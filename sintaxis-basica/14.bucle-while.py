# el cilo while se ejecut miestras una condicion 
# sea verdadera o falsa de manera infinita

# edad = int(input("Introduce tu edad porfavor: "))

# while edad<0:
#     print("Has introducido una edad negativa, vuelve a intentarlo")
#     edad = int(input("Introduce tu edad porfavor: "))

import math
    
print("Programa para el calculo de la raiz cuadrada")
numero = int(input("Introduce un numero por favor: "))

intentos = 0
if intentos==0:
    while numero < 0:
        print("No se puede calcular la raiz cuadrada de un numero negativo")
        intentos+=1
        numero = int(input("Introduce un numero por favor: "))
        if numero < 0:
            intentos+=1
        
        if intentos == 2:
            print("Has consumido todos tus intentos diarios")
      
if intentos<2:
    solucion =math.sqrt(numero)
    print(f"la raiz cuadrada de {numero} es {solucion}")