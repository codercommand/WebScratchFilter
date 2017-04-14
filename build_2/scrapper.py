import inteligent_filter as IF
import decripter as de
import urllib.request
import json

def scrapper(urlsearch, template, exc):
    scrapped = []
    with urllib.request.urlopen(urlsearch) as response:
        with open(template, 'r') as file:
            for x in IF.IN_FI(de.decripter(response.read().decode('utf-8')),
                              json.loads(file.read())):
                scrapped.append(x)

    result = []
    for x in scrapped:
        z = len('a href="{}'.format(exc))
        a = z
        while x[0][a] != '"':
            a += 1
        result.append(x[0][z:a])

    return result

if __name__ == '__main__':
    for x in scrapper(input('url to scrape: '),
                   input('template filter: '),
                   input('give part of url to excood: '),
                      ):
        print(x)
