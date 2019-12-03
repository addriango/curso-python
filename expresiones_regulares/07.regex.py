#las funciones match y

import re
nombre1="sandra lopez"
nombre2="antonio gomez"
nombre3="maria lopez"

#encuentra si  nombre2 empieza  por sandra (diferencia minusculas y mayusculas)
if re.match("sandra",nombre2):
    print("Hemos encontrado el nombre")
else:
    print("no lo hemos encontrado")
    

cadena1="pablo medina"
cadena2="2323233"
cadena3="54334"

print("")
#encuentra si el cadena2 empeza por digitos
if re.match("\d",cadena2):
    print("Hemos encontrado el numero")
else:
    print("no lo hemos encontrado")
