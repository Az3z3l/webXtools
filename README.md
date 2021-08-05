# webXtools

A wouldbe toolset for web exploitation and other general tools used in CTFs. 

## To install

`pip3 install webXtools`


## Modules

* [Bruteforcer](#bruteforce)
* [Race Condition](#race-condition)
* [JWT](#jwt)

## Usage

### Bruteforce
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


# bruteforceList
def doit(st):
    # something with the string 
    return False

webXtools.bruteforceList(stringList=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], noOfThreads=5, callback=doit)


# bruteforceFile
webXtools.bruteforceFile(file="./payloads.txt", noOfThreads=5, callback=check)

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

### JWT

```py
import webXtools
import string

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.R6zywlgNMEEcoM01FyTd3XY-iODzr-uvpWWw9i8VHho"

print(webXtools.jwtHS256Brute(token, charSet=string.ascii_letters, maxLength=3))

print(webXtools.jwtHS256Brute(token, stringList=["a", "c", "abs"]))

print(webXtools.jwtHS256Brute(token, stringFile="./strings.txt", noOfThreads=10))
```

