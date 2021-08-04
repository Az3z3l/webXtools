from webXtools.bf import bruteforce
from webXtools.helper import splitFile
import hmac, base64, hashlib, string

genToken = lambda secret, content: (base64.b64encode(hmac.new(secret.encode(), content.encode(), digestmod = hashlib.sha256).digest()).decode('ascii')).replace("=", "").replace("+", "-").replace("/", "_")


def jwtBrute(token:str, minLength=1, maxLength=4, charSet=string.ascii_letters+string.digits, file="", list=[], noOfThreads=1):
    """Crack a JWT either using a blind string bruteforce or a file of words or a list of words

    Args:
        token (str): The JWT
        minLength (int, optional): Minimum length of string to bruteforce. Defaults to 1.
        maxLength (int, optional): Maximum length of string to bruteforce. Defaults to 4.
        charSet (string, optional): The character set. Defaults to string.ascii_letters+string.digits.
        file (str, optional): Use the words present in the file. Takes higher precedence than charSet if defined. Defaults to "".
        list (list, optional): Use the words present in the file. Takes higher precedence than file if defined. Defaults to [].
        noOfThreads (int, optional): Number of threads to use. Defaults to 1.
    Returns:
        str or None: Returns the secret key if it was bruteforced or returns None
    """
    

    header, data, sign = token.split(".")
    content = f"{header}.{data}"

    def checker(secret):
        currHash = genToken(secret, content)
        if currHash == sign:
            return True
        else:
            return False
    


        
        
        
    return(bruteforce(minLength, maxLength, charSet, noOfThreads, checker))

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.R6zywlgNMEEcoM01FyTd3XY-iODzr-uvpWWw9i8VHho"
print(jwtBrute(token))