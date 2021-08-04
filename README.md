# webXtools

A wouldbe toolset for web exploitation and other general tools used in CTFs. 

## To install

`pip3 install webXtools`

## Usage

### String Bruteforcer
A multithreaded approach to generate strings

```py
import webXtools
import hashlib
import string

# Find a string such that `hashlib.sha256("string".encode('utf-8')).hexdigest()[:5]` returns `3f6ac`


def check(string):
    if hashlib.sha256(string.encode('utf-8')).hexdigest()[:5] == "3f6a4":
        return True
    else:
        return False

# Returns the string that solves callback
print(webXtools.bruteforce(minLength=1, maxLength=4, charSet=string.ascii_letters+string.digits, noOfThreads=4, callback=check))

# Prints all the strings generated
webXtools.bruteforce(minLength=1, maxLength=4, charSet=string.ascii_letters+string.digits, noOfThreads=4, callback=print)
```

### Race Condition
Test race condition in Web Applications

```py
import webXtools

# 1
r = webXtools.race(url="https://google.com", numberOfRequests=100, threads=5)
## r has a list of all the responses


# 2
webXtools.race(url="http://vuln.com", cookies={"id":"evil"}, method="GET", headers={"iam":"admin"}, numberOfRequests=200, threads=10)


# 3
request = """POST /test/ HTTP/1.1
HOST: localhost:1337
Content-Type: application/JSON
Content-Length: 15

{"test":"data"}
"""
webXtools.race(url="http://localhost:1337", absoluteRequest=request, threads=5)
```