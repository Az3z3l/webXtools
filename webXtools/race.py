import socket
from urllib.parse import urlparse
from threading import Thread
import asyncio
import ssl

global results, clients

results = list()
clients = list()

def createRequest(url, jar, method, data="", customHeaders={}):
    parser = urlparse(url)
    global targetPort, targetHost
    try:
        targetHost = parser.netloc.split(":")[0]
        targetPort = parser.netloc.split(":")[1] 
    except:
        targetHost = parser.netloc
        targetPort = 80 if (parser.scheme == "http") else 443

    cookies = ""
    for j in  jar:
        cookies += f"{j}={jar[j]};"

    headers = ""
    for h in customHeaders:
        headers+=f"{h}: {customHeaders[h]}\r\n"

    path  = "/" if parser.path == "" else parser.path
    path += "" if parser.query == "" else f"?{parser.query}"
    path += "" if parser.fragment == "" else f"#{parser.fragment}"


    # send some data 
    req = f"{method} {path} HTTP/1.1\r\n"
    req += "Host: "+ targetHost + "\r\n"

    req += "cookie: "+ cookies + "\r\n" if (cookies != "") else ""

    req += "Connection: Keep-Alive\r\n"

    req += "Content-Length: "+ str(len(data)) +"\r\n" if len(data)>0 else "\r\n"
    req += headers
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
            context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
            client = context.wrap_socket(client, server_hostname=targetHost)

        # connect the client 
        client.connect((targetHost,int(targetPort)))  

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((targetHost,int(targetPort)))
        clients.append(client)

def threadifyCreate(req, threads, totalNumberOfrequests):
    """Create number of requests needed to be sent from thread

    Args:
        req (string): Request content to be sent
        threads (int): Number of threads to use
        totalNumberOfrequests (int): Number of requests to send
    """
    th = list()
    requestsInThread = totalNumberOfrequests // threads
    global request
    request = (bytes(req, "utf-8"))
    for i in range(threads):
        t1 = Thread(target=threadHandler, args=[requestsInThread])
        th.append(t1)
    for i in th:
        i.start()
    for i in th:
       i.join()
    
def threadifySend(threads, totalNumberOfrequests):
    """Send requests from the clients

    Args:
        req (string): Request content to be sent
        threads (int): Number of threads to use
        totalNumberOfrequests (int): Number of requests to send
    """
    th = list()
    requestsInThread = totalNumberOfrequests // threads
    start=0
    for i in range(threads):
        t1 = Thread(target=asyncio.run, args=[awaiter(start,start+requestsInThread)])
        start+=requestsInThread
        th.append(t1)
    for i in th:
        i.start()
    for i in th:
       i.join()


totalNumberOfrequests = 200
threads = 5
url = "http://localhost:8000"
jar = {"name1":"value1", "name2":"value2"}
data = ""
method = "GET"
customHeaders = {}

req = createRequest(url,jar,method)

# create threads
threadifyCreate(req, threads, totalNumberOfrequests)

# run threads after creating them
threadifySend(threads, totalNumberOfrequests)

print("done")