## los bucles nos ayudan a ejecutar codigo repetitivo en pocas lineas

##esto no es eficiente
print ("hola mundo")
print ("hola mundo")
print ("hola mundo")
print ("hola mundo")

print("")
##esto si es eficiente

##bucle determianado (sabemos cuantas veces se va a realizar)
for cadaNumero in range(4):
    print (cadaNumero)

print("")

##recorrer un string con bucle determinado
user_email = input("Introduce tu email: ")
contador_email = 0
for cadaLetra in user_email:
    if cadaLetra == "@":
        contador_email+=1
    if cadaLetra == ".":
        contador_email+=1 
if contador_email == 2:
    print("Email correcto")
else:
    print("Email incorrecto")


print("")
#bucle indetermiando, no sabemos (recorre toda la lista)
nombres = ["pablo","maria","juana","johan","miguel"]
for nombre in nombres:
    print(nombre)

