import re

lista=[
    'Ma1',
    'Se1',
    'Ma2',
    'Ba1',
    'Ma3',
    'Va1',
    'va2',
    'Ma4',
    'MaA',
    'Ma5',
    'MaB',
    'Mac'
]

#busca element que comienzen por Ma y seguido tengan un
#rango entre0 y 3, o entre A y B
for elemento in lista:
    if re.findall('Ma[0-3A-B]',elemento):
        print(elemento)