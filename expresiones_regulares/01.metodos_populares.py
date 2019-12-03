#regex son una secuencia de caracteres que forman un patron de busqueda

import re

cadena="vamos a aprender expresiones regulares y aprender a programar mucho mas"

#metodo search
# if re.search("aprender",cadena) is not None:
#     print("encontre lo que buscabas")
# else:
#     print("no encontre nada")

textobuscar="aprender"
textoencontrado = re.search(textobuscar,cadena)


#el metodo start() devuelve el numero indice donde encontro la coincidencia)
print(textoencontrado.start())
print(textoencontrado.end()) #donde termina
print(textoencontrado.span()) #hace dos en uno,donde empieza y termina

#el metodo findall devuelve una lista con todas las palabras que coinciden
print(len(re.findall(textobuscar,cadena)))