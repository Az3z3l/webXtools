import webXtools
import hashlib
import string
import time

# Find a string such that `hashlib.sha256("string".encode('utf-8')).hexdigest()[:5]` returns `3f6ac`


def check(string):
    if hashlib.sha256(string.encode('utf-8')).hexdigest()[:5] == "3f6a4":
        return True
    else:
        return False

start = time.time()
print(webXtools.bruteforce(minLength=1, maxLength=4, charSet=string.ascii_letters+string.digits, noOfThreads=4, callback=check))
end = time.time()

print(f"Runtime of the program is {end - start}")


def doit(st):
    # something with the string 
    return False

webXtools.bruteforceList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], noOfThreads=5, callback=doit)
