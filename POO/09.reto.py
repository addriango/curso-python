#crear un programa que pida introducir una direccion email por teclado
#el programa debe imprimir por consola si la direccion de email es correcta
# o no en funcion de si esta tiene el simbolo "@". Si tiene un arroba la direccion
#sera correcta.Si tiene mas de una o ninguna "@" sera erronea
# sila "@" esta al comienzo de la direccion email tambien sera erronea

email=input("Introduce tu Email: ")

ultimocaracter=len(email)-1
veces=email.count("@")
posicion_arroba=email.find("@")

if veces==0 or veces>1 or posicion_arroba==0 or posicion_arroba==ultimocaracter:
    print("El email es incorrecto")
else:
    print("El email es correcto")
    
#solucion con metodos string

# mailUsuario=input("Introduce tu Email: ")

# arroba=mailUsuario.count("@")

# if arroba!=1 or mailUsuario.rfind("@")==(len(mailUsuario)-1) or mailUsuario.find("@")==0:
#     print("Email incorrecto")
# else:
#     print("Email Correcto")
    
    