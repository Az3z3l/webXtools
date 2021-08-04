

def splitFile(toOpen):
    filee = open(toOpen, "r")
    content = filee.read()
    filee.close()
    print(content)
    content_list = content.split("\n")
    return content_list
