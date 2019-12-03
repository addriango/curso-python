#Operaciones con strings

## metodo upper() convierte todos los caracteres a mayuscula
## metodo lower() convierte todos los caracteres a minuscula
## metodo capitalize() convierte la primera letra en mayuscula
## metodo count() cuenta cuantas veces aparece un caracter en un texto
## metodo find() representar la posicion de un caracter dentro de un texto
##metodo isdigit() devuelve true o false si es numerico o no
## metodo isalum() devuelve true o false si es alfanumerico o no
## metodo isalpha() devuelve true o false si son solo letras
## metodo split() separa por palabras usando espacios
## metodo strip() borra los espacios sobrantes al principio y al final
## metodo replace() cambia una palabra o una letra por otra dentro de un texto
## metodo rfind() representar la posicion de un caracter dentro de un texto con-
##tando desde atras

# nombreUsuario=input("Introduce tu nombre: ")

# print(nombreUsuario.upper()) #mayusculas
# print(nombreUsuario.lower()) #miyusculas
# print(nombreUsuario.capitalize()) #primer caracter mayuscula

edad=input("cual es tu edad?: ")

print(edad.isdigit())