import string
import math  
from threading import Thread

def bruteforce(minLength=1, maxLength=4, charSet=string.ascii_letters+string.digits, noOfThreads=1, callback=print, debug=False):
    """Generates all possible characters within the given chars and length

    Args:
        minLength (int, optional): Minimum length of string to bruteforce. Defaults to 1.
        maxLength (int, optional): Maximum length of string to bruteforce. Defaults to 4.
        charSet (string, optional): The character set. Defaults to string.ascii_letters+string.digits.
        noOfThreads (int, optional): Number of threads to use. Defaults to 1.
        callback (function, optional): Callback function. Defaults to print.
        debug (bool, optional): Set to True if all chars needed to be printed. Defaults to False
    Returns:
        str or None: Returns the String that was used for solving by callback
    """
    def listToChar(l):
        string = ""
        for s in l:
            string += charSet[s]
        return string


    def nextChar(curr):
        for idx in range(len(curr)):
            if curr[idx] == lastChar:
                curr[idx] = 0
                if idx == (len(curr)-1):
                    curr = [0]+curr
            else:
                curr[idx] += 1
                break
        return curr

    def checker(string):
        if (debug and callback!=print):
            print(string)
        a = callback(string)
        if a==True:
            global stop, finale
            finale = string
            stop = True
            return True
        else:
            return False


    def start(init,fin):
        curr = init
        fin = nextChar(fin)
        i=0
        while(i < tlen):
            if stop:
                return
            checker(listToChar(curr))
            curr = nextChar(curr)
            i += 1

    def adder(arr, value):
        li = arr
        top = lenChars
        rem = 0 
        quo = 0
        idx = 0
        while True:
            t = li[idx]+value
            rem = t % top
            quo = t // top
            li[idx]=rem
            if quo>0 and idx==(len(li)-1):
                quo -= 1
                li = li + [0]
                
            value = quo
            if idx == len(li)-1:
                break
            idx += 1
        return (li)

    def splitter(to):
        possibilities = 0
        for i in range(minLength,maxLength+1):
            possibilities = possibilities + (lenChars**i)
            if possibilities<noOfThreads:
                raise Exception("Number of threads greater than the bruteforce possibilities")
        global tlen
        tlen = math.ceil(possibilities/to)
        first = [0]*minLength
        now = first
        completed = 0
        fin = list()
        while completed < possibilities:
            temp=[]
            temp += [now[:]] 
            curr = adder(now,tlen)
            temp.append(curr[:])
            now = curr
            fin+=[temp[:]]
            completed += tlen
        return fin



    def threadify(lists):
        th = list()
        for i in lists:
            t1 = Thread(target=start, args=(i), name=f"thread-{i}")
            th.append(t1)

        for i in th:
            i.start()
            
        for i in th:
            i.join()

    global stop
    stop = False
    lenChars = len(charSet)
    lastChar = lenChars-1
    lists = splitter(noOfThreads)
    threadify(lists)
    try:
        return(finale)
    except:
        return(None)


def bruteforceList(stringList, noOfThreads=1, callback=print, debug=False):
    """Given a list iterates that and calls callback for each item

    Args:
        stringList (list): The list of strings
        noOfThreads (int, optional): Number of threads to use. Defaults to 1.
        callback (function, optional): Callback function. Defaults to print.
        debug (bool, optional): Set to True if all chars needed to be printed. Defaults to False
    Returns:
        str or None: Returns the String that was used for solving by callback
    """
    def start(currList):
        for i in currList:
            if stop:
                return
            checker(i)

    def checker(string):
        if (debug and callback!=print):
            print(string)
        a = callback(string)
        if a==True:
            global stop, finale
            finale = string
            stop = True
            return True
        else:
            return False

    def splitter():
        if noOfThreads<=1:
            return [stringList]
        tlen = math.ceil(lenlist/noOfThreads)
        lists = []
        i = 0 
        while(i<lenlist-tlen):
            lists.append(stringList[i:i+tlen])
            i += tlen
        lists[-1]+=stringList[i::]
        return lists

    def threadify(lists):
        th = list()
        for i in lists:
            t1 = Thread(target=start, args=(i, ))
            th.append(t1)

        for i in th:
            i.start()
            
        for i in th:
            i.join()


    lenlist = len(stringList)

    if lenlist<noOfThreads:
        raise Exception("Number of threads greater than the number of strings given")

    global stop
    stop = False
    tlists = splitter()
    threadify(tlists)
    try:
        return(finale)
    except:
        return(None)


def bruteforceFile(file, noOfThreads=1, callback=print, debug=False):
    """Given a file, iterates that and calls callback for each item

    Args:
        file (str): Location of file
        noOfThreads (int, optional): Number of threads to use. Defaults to 1.
        callback (function, optional): Callback function. Defaults to print.
        debug (bool, optional): Set to True if all chars needed to be printed. Defaults to False
    Returns:
        str or None: Returns the String that was used for solving by callback
    """
    from webXtools.helper import splitFile
    stringList = splitFile(file)
    return(bruteforceList(stringList, noOfThreads, callback, debug))


