import socket
from urllib.parse import urlparse
from threading import Thread
import asyncio
import ssl
import time


def race(url="", cookies={}, method="GET", data="", headers={}, absoluteRequest="", numberOfRequests=100, threads=1):
    """Generate a ton of requests in a short span of time to test race condition in a page

    Args:
        url (str): Url of the server to send request.
        cookies (dict, optional): Any cookies to add. Defaults to {}.
        method (str, optional): The request method. Defaults to "GET".
        data (str, optional): Any data to be sent with the request. Defaults to "".
        headers (dict, optional): Additional headers to be sent. Please note to send the content-type or other necessary headers. Defaults to {}.
        absoluteRequest (str, optional): Create your own request and not use the other arguments provided. Defaults to "".
        numberOfRequests (int, optional): Number of requests to send. Defaults to 0.
        threads (int, optional): Number of threads to use. Defaults to 1.
    Returns:
        list: The responses for all the requests made
    """

    def createRequest():
        cookiesz = ""
        for j in  cookies:
            cookiesz += f"{j}={cookies[j]};"

        headersz = ""
        for h in headers:
            headersz+=f"{h}: {headers[h]}\r\n"

        path  = "/" if parser.path == "" else parser.path
        path += "" if parser.query == "" else f"?{parser.query}"
        path += "" if parser.fragment == "" else f"#{parser.fragment}"


        # send some data 
        req = f"{method} {path} HTTP/1.1\r\n"
        req += "Host: "+ targetHost + "\r\n"

        req += "cookie: "+ cookiesz + "\r\n" if (cookiesz != "") else ""

        req += "Connection: Keep-Alive\r\n"

        req += "Content-Length: "+ str(len(data)) +"\r\n" if len(data)>0 else "\r\n"
        req += headersz
        req += "\r\n"
        req += data
        req += "\r\n\r\n"
        return req


    async def clientIndividualSend(client):
        client.send(request)
        result = client.recv(6000)
        results.append(result)
        
    async def awaiter(start, end):
        tasks = list()

        for client in clients[start:end]:
                temp = asyncio.create_task(clientIndividualSend(client))
                tasks.append(temp)

        [(await task) for task in tasks]


    def threadHandler(requestsInThread):
        """Create the clients

        Args:
            requestsInThread (int): Number of requests in this thread 
        """
        for _ in range(requestsInThread):
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

            if targetPort == 443:
                context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
                client = context.wrap_socket(client, server_hostname=targetHost)

            # connect the client 
            client.connect((targetHost,int(targetPort)))  

            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((targetHost,int(targetPort)))
            clients.append(client)

    def threadifyCreate():
        """Create number of requests needed to be sent from thread

       
        """
        th = list()
        requestsInThread = numberOfRequests // threads
        global request
        request = (bytes(req, "utf-8"))
        for i in range(threads):
            t1 = Thread(target=threadHandler, args=[requestsInThread])
            th.append(t1)
        for i in th:
            i.start()
        for i in th:
            i.join()
        
    def threadifySend():
        """Send requests from the clients

        Args:
            req (string): Request content to be sent
            threads (int): Number of threads to use
            numberOfRequests (int): Number of requests to send
        """
        th = list()
        requestsInThread = numberOfRequests // threads
        start=0
        for i in range(threads):
            t1 = Thread(target=asyncio.run, args=[awaiter(start,start+requestsInThread)])
            start+=requestsInThread
            th.append(t1)
        for i in th:
            i.start()
        for i in th:
            i.join()

    def uri_validator(x):
        try:
            return all([parser.scheme, parser.netloc])
        except:
            return False

    results = list()
    clients = list()
   
    parser = urlparse(url)
   
    if not uri_validator(url):
        raise Exception("Provided an improper URL")


    try:
        targetHost = parser.netloc.split(":")[0]
        targetPort = parser.netloc.split(":")[1] 
    except:
        targetHost = parser.netloc
        targetPort = 80 if (parser.scheme == "http") else 443
    

    

    req = absoluteRequest if absoluteRequest!="" else createRequest()

    # create threads
    print("### Generating the Requests ###")
    threadifyCreate()

    # run threads after creating them
    print("### Starting Exploit ###")
    start = time.time()
    threadifySend()
    end = time.time()

    print(f"All requests sent in {end - start}s")