import re

lista_nombres=[
    'Ana',
    'pedro',
    'maria',
    'rosa',
    'sandra',
    'celia'
]

# nombres que tienen las letras de la "o" ala "t", [o,p,q,r,s,t]
# se us [primeraracter-ultimocaracter]
for elemento in lista_nombres:
    if re.findall('[o-t]',elemento):
        print(elemento)

print("")
#nombres que termien con o,p,q,r,s ó t      
for elemento in lista_nombres:
    if re.findall('[o-t]$',elemento):
        print(elemento)  