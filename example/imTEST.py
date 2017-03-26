import decripter as de
import inteligent_filter as IF
import json


for x in ['testSITE.html', 'testSITE-2.html']:
    with open(x, 'r') as f:
        with open('k.txt', 'r') as file:
            for i in IF.IN_FI(de.decripter(f.read()), json.loads(file.read())):
                print(i)
