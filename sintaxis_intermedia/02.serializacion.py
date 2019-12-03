# serializacion consiste en guardar en un archivo externo
# una lista, una coleccion, un objeto, pero la particularidad
# es que lo guardamos codificado en codigo binario

#biblioteca necesaria Pickle

#esta libreria tiene dos metodos:
## el metodo dump(): volcado de datos al fichero binario externo
## metodo load(): carga de los datos del fichero binario externo

import pickle

lista_nombres=["pedro","ana","maria","isabel"]

# "w":lectura
# "r":escritura
# "wb": escritura binaria
# "rb": lectura binaria
# "a": añdir 
# "ab": añdir binario

fichero_binario=open("lista_nombres","wb")

pickle.dump(lista_nombres,fichero_binario)

fichero_binario.close()
del (fichero_binario)