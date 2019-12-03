import re

lista_nombres=[
    'hombres',
    'mujeres',
    'mascotas',
    'niños',
    'niñas'
]

#busca las palabras niños o niñas
#dentro de [oa] se colocan los dos valores que varian
for elemento in lista_nombres:
    if re.findall('niñ[oa]s',elemento):
        print(elemento)
        
lista_cosas=[
    'hombres',
    'mujeres',
    'mascotas',
    'camión',
    'camion'
]

#busca las palabra camion con tilde o sin tilde
#dentro de [oó] se colocan los dos valores que varian
for elemento in lista_nombres:
    if re.findall('cami[óo]n',elemento):
        print(elemento)