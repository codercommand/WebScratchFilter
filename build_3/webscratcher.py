import urllib.request
import json

class WS:

    def extract(l_url, m_url=''):
        """
        This is a generator.
        Its job is to take urls and return their html
        data.

        The first value is the main url if you need it.
        And the second is the products url.

        Here if I have product url that looks like this:
        /product/tea-bags/
        The url is missing its beginning part which look a
        little like this: "https://www.teashop.com/"
        So we need to give that first part of the url so
        it can find the product.
        But if it has all its url you don't need to give
        the main url, example: "https://www.google.com/gmail/Soul/"
        See it has its whole url? we don't need to give any
        main url cause of that.

        I used a generator so you can save to hard drive as you
        proccess the data. Cause otherwise it will be a little
        rammy cause it would return lists which would not return
        until its finished fishing. Thats alot of data to store
        :P 
        """
        #This for loop compiles the urls so if they need a main
        #it adds it to the url so we can go fishing for out data!
        temp = []
        for x in l_url:
            temp.append(m_url+x)

        #A is an un needed varible.
        #Its used to help tell us how
        #many urls have been extracted so far.
        a = 0
        for x in temp:
            print(str(a)+' "'+x+'"')
            print()
            
            #This part does all the fishing for us
            with urllib.request.urlopen(x) as response:
                yield response.read().decode('utf-8')
                
            a += 1

    def scratch(urlsearch, template, exc):
        """
        Use this function to extract product urls from a page.
        
        First value is the url of the page to search for product
        urls. Second is the template, use that to try and get the
        urls you want. It must have at least something passed through
        or else it wont find any urls! And the last third value is
        from left to right what part of the url to not include.
        Cause otherwise you can get unwanted wast.

        Example:
        http://www.google.com/youtube/dave
        say we are going through urls and we want the
        name of the youtuber but not the google and youtube
        part? well we would give a value like "http://www.google.com/youtube/"
        and now all that will be returned is dave.
        """
        scrapped = []
        with urllib.request.urlopen(urlsearch) as response:
            with open(template) as file:
                for x in WS.int_fil(WS.decripter(response.read().decode('utf-8')),
                                              json.loads(file.read())):
                    scrapped.append(x)

        result =[]
        for x in scrapped:
            z = len('a href="{}'.format(exc))
            a = z
            while x[0][a] != '"':
                a += 1
            result.append(x[0][z:a])

        #It deletes all url copys by making a set.
        #Then it changes back to a list so its a usable
        #format for anyone using it.
        return list(set(result))

    def int_fil(html, template):
        """
        This is a filter to extract the data we want from our
        decripted files. Example of input:
        print(INT_filter([['p','Hello',0],['h1','World',1],['div','!',2]],
               {'filter':[['p',1],['h1',2]]}))
        And the output is:
        [['p', 'Hello', 0], ['h1', 'World', 1]]

        The first value is the data, the second is the filter data.
        When you parse data through send a array of arrays that contain
        three values. two string and one number. Example:
        [
            ['p', 'hello world', 0],
            ['h1 style="..."', 'I love you!', 1]
        ]
        """
        #extracted data varible
        datafilterd = []
        tl = 0
        while tl != len(template['filter']):
            x = 0
            while x != len(html):
                #x is the postition in the list(array), [0] is the tag in the list's
                #list. And [:len(...)] takes a string slice from the tag so we
                #can test to see if it matches the filter
                if html[x][0][:len(template['filter'][tl])] == template['filter'][tl]:
                    datafilterd.append(html[x])
                x += 1
            tl+= 1

        #returns extracted data varible
        return datafilterd
    
    def decripter(html):
        """
        This is the decripter api
        """

        def __INDEX__(html):
            """
            The job of this function is to append an
            index to the end of each tag.
            """
            x = 0
            while x != len(html):
                html[x].append(x)
                x += 1

            return html

        def __EXTRACT__(html):
            """
            The job of the function is to delete
            all \n from the HTML string.
            """
            data = ''
            temp = []
            #changes string to list
            for x in range(len(html)):
                temp.append(html[x])

            #deletes all \n from list
            x = 0
            temp2 = []
            while x != len(temp):
                if temp[x] != '\n':
                    temp2.append(temp[x])
                x += 1
            del x

            #changes list back to string
            for x in temp2:
                data = data + x

            #returns string
            return data

        def __DECRIPT__(html):
            """
            This function decriptes HTML to list of lists.
            The result is something like this:
            [
                ['h1', 'hello world', 0],
                ['p style="..."', 'This product is...', 1]
            ]
            """
            line = []

            for x in range(len(html)):

                #This is the gate. It makes sure we are seeing tags
                if html[x:x+2] != '</':
                    if html[x] == '<':

                        #grabs tag name
                        temp = x
                        while html[temp] != '>':
                            temp += 1

                        #Grads tags content. If it sees an ending nested
                        #tag is will think its done even though is hasn't
                        #got everything
                        temp2 = temp
                        while html[temp2:temp2+2] != '</':
                            temp2 += 1

                        #Appends content to line
                        line.append([html[x+1:temp], html[temp+1:temp2]])

            #Returns list of decripted html
            return line

        return __INDEX__(__DECRIPT__(__EXTRACT__(html)))


if __name__ == '__main__':
    x = 0
    for html in WS.extract(WS.scratch("http://international.muscletech.com/products/",
                                      "sup.txt",
                                      ""),
                           "http://international.muscletech.com"):
        _html = WS.int_fil(WS.decripter(html), {'filter': ["div id=\"mk-text-block-"]})

        with open('data/'+str(x), 'w') as f:
            _html = json.dumps({'data': _html})
            f.write(_html)

        x += 1
        
        if not x < 6:
            break
