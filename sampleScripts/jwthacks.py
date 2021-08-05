import webXtools
import string

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.R6zywlgNMEEcoM01FyTd3XY-iODzr-uvpWWw9i8VHho"

print(webXtools.jwtHS256Brute(token, charSet=string.ascii_letters, maxLength=3))

print(webXtools.jwtHS256Brute(token, stringList=["a", "c", "abs"]))

print(webXtools.jwtHS256Brute(token, stringFile="./strings.txt", noOfThreads=10))


