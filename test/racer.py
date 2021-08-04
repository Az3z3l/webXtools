import webXtools

webXtools.race(url="https://google.com", numberOfRequests=100, threads=5)


request = """POST /test/ HTTP/1.1
HOST: localhost:1337
Content-Type: application/JSON
Content-Length: 15

{"test":"data"}
"""
webXtools.race(url="http://localhost:1337", absoluteRequest=request, threads=5)


webXtools.race(url="http://vuln.com", cookies={"id":"evil"}, method="GET", headers={"iam":"admin"}, numberOfRequests=200, threads=10)