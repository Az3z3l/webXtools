import webXtools
import hashlib
import string


# Find a string such that `hashlib.sha256("string".encode('utf-8')).hexdigest()[:4]` returns `7c21`


def check(string):
    if hashlib.sha256(string.encode('utf-8')).hexdigest()[:4] == "7c21":
        return True
    else:
        return False

value = webXtools.bruteforce(minLength=1, maxLength=4, charSet=string.ascii_letters+string.digits, noOfThreads=3, callback=check)

print(value)