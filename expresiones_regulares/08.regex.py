#la funcion search a diferencia dela funcion match no busca
# solo al principio si no en toda la cadena

import re

nombre1="jara lopez medina"
nombre2="antonio gomez lopez"
nombre3="lara funetes gomez"

if re.search("lopez",nombre2):
    print("hemos encontrado el nombre")
    
else:
    print("no lo hemos encontrado")