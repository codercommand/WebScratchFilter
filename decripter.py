def decripter(HTML):
    """
    This is the decripter api
    """
    return __TREEindex(__decripter(__spliter(HTML)))


def __TREEindex(page):
    """
    The job of this function is to append an index to the end of
    each tag.
    """
    x = 0
    while x != len(page):
        page[x].append(x)
        x += 1

    return page


def __spliter(HTML):
    """
    The job of this function is to delete all \n from the HTML string
    """
    data = ''
    temp = []
    #changes string to list
    for x in range(len(HTML)):
        temp.append(HTML[x])

    #deletes all \n from list
    x = 0
    while x != len(temp):
        if temp[x] == '\n':
            del temp[x]
        x += 1
    del x

    #changes list back to string
    for x in temp:
        data = data + x

    #returns string
    return data

    
def __decripter(HTML):
    """
    This function decriptes HTML to a Json object.
    It decriptes into a TREE format. The result is
    something like this:
    [
        ['h1', 'Hello, world', 1],
        ['p style="..."', 'This product is...', 2]
    ]
    """
    page = []
            
    for x in range(len(HTML)):

        #This is the gate. It makes sure we are seeing tags
        if HTML[x:x+2] != '</':
            if HTML[x] == '<':

                #grabs tag name
                temp = x
                while HTML[temp] != '>':
                    temp += 1

                #Grabs tags content. If it sees an ending nested
                #tag it will think its done even though it hasn't
                #got everything
                temp2 = temp
                while HTML[temp2:temp2+2] != '</':
                    temp2 += 1

                #Appends content to page.
                page.append([HTML[x+1:temp], HTML[temp+1:temp2]])

    #returns array of decripted HTML
    return page


if __name__ == '__main__':
    uc = input('file name: ')
    with open(uc, 'r') as f:
        data = f.read()
        
    i = __TREEindex(__decripter(__spliter(data)))
    x = 0
    while x != len(i):
        print(i[x])
        x += 1

    
