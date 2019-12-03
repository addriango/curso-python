import re 

lista_nombres=[
    'Ana Gomez',
    'Maria Martin',
    'Sandra Lopez',
    'Santiago Martin'
]

for elemento in lista_nombres:
    if re.findall('Martin$',elemento):
        print(elemento)
        

# ^sandra  #que comienzen por sandra 
# sandra$  #que terminen por sandra 
# ^sandra$  #que comienzen y terminen por sandra 
