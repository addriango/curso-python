miLista = ["maria","pepe","sebastian","antonio"] #se cuenta la posicion desde cero 

print(miLista[0]) # imprime el primer item en orden 

print(miLista[2]) #imprime el tercer item en orden

print(miLista[:]) #imprime todos los item de la lista

print(miLista[-1]) # imprime el primer item en orden inverso (el ultimo)

print(miLista[-2]) # imprime el segundo item en orden inverso (antes del ultimo)

# [incluye:excluye]

print(miLista[0:3]) #desde la posicion cero hasta 2 / una posicion antes del ultmo valor

print(miLista[:4]) #imprime los dos primeros

print(miLista[1:3]) # imprime pepe y marta

miLista.append("sandra") #agrega un item mas alfinal de la lista

miLista.insert(2,"lucas") #incluye un item en la posicion especificada

miLista.extend(["pablo","leonel","lucia"]) #concatena varios elemetos al final de la lista

miLista.index("pepe") # en que posicion esta pepe en la lista (contando desde cero)

print("pepe" in miLista) #imprime true si pepe esta en miLista o false si no esta

miLista.remove("antonio") #elimina el item pasado en una lista

miLista.pop() #elimina el ultimo valor de la lista

nombres1 = ["johan","angel","simon"]
nombres2 = ["luisa","esteban","carlota"]

nombresTotal = nombres1 + nombres2  #la suma de dos lista concatena una con la otra

nuevaLista = nombres1 * 3  #repite la lista 3 veces
print(nuevaLista)
