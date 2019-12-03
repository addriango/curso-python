# para tener persistencia de datos, es decir que no borren
# tenemos dos alternativas: 1.es trabajar con arvhivos externos
# y 2. es trabajar con bases de datos

#el metodo open nos permite abrir un archivo nuevo y si no existe lo crea
from io import open

#recibe dos parametros: el nombre del archivo y el modo "w":escritura 
# o "r":lectura o "a":modo append, para agregar algo al archivo

#archivo_texto=open("archivo.txt","w")
archivo_texto=open("archivo.txt","r")
# archivo_texto=open("archivo.txt","a")

#frase="Excelentia dia para estudiar python \n el domingo"
# archivo_texto.write(frase)

# frase="\nnunca pares de crecer"
# archivo_texto.write(frase)

#el metodo read nos permite leer todo el archivo
#el metodo readline nos perite leer linea a linea
#el metodo write nos permite escribir un archivo completo y reemplaza
#el contenido si ya existe dicho archivo
#el metodo writelines nos permite escribir linea a linea
#el metodo seek nos permite posicionar el cursor en el archivo

texto=archivo_texto.read()
# lineas=archivo_texto.readlines()

print(texto)
texto=archivo_texto.read()

archivo_texto.close()
print(texto)

#numero de elementos del array/numero de lineas del arvhivo
# print(len(lineas))

#imprimirprimera linea
# print(lineas[0])


# print(lineas)