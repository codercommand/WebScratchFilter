import decripter as de
import json


#name of file to filter
uc = input('file name: ')
with open(uc, 'r') as f:
    uc = f.read()


#name of product type    
ucc = input('product type: ')


#decripting HTML into TREE for use
TREE = {} 
TREE[ucc] = de.decripter(uc)


datafilter = []


#This is the template filter. It will extract all the html tags we want
with open(input('template file name: '), 'r') as f:
    template = json.loads(f.read())


tl = 0
while tl != len(template['filter']):
    x = 0
    while x != len(TREE[ucc]):
        if TREE[ucc][x][0][0:template['filter'][tl][1]] == template['filter'][tl][0]:
            datafilter.append(TREE[ucc][x])
        x += 1
    tl += 1

for x in datafilter:
    print(x)
