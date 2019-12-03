numero1 = 4
numero2 = 7

if numero1 < numero2: 
    print("el numero1 es menor")

if numero1 > numero2:
    print("el numero 1 es mayor")

if numero2 == numero1:
    print("ambos numeros son iguales if")
elif numero2 < numero1:
    print("el numero 2 es menor dentro de elif")
else:
    print("no son iguales")
    
print("programa de evaluacion de alumnos")
nota_alumno = input("introduce la nota: ")

def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="reprobado"
    return valoracion

print(evaluacion(int(nota_alumno)))