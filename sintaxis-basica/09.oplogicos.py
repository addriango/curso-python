## python a diferencia de otros lenguajes puede concatenar
## operadores de comparacion

# edad = 7

# if 0<edad<100:
#     print("edad esta entre 0 y 100")
# else:
#     print("edad incorrecta")

## progarama que evalua salarios

salario_presidente=int(input("Introduce el salario del presidente"))
#en python no se puede concatenar datos de diferentes tipos (hay que convertirlo)
print("Salario presidente: " + str(salario_presidente))

salario_director=int(input("Introduce el salario del director"))
#en python no se puede concatenar datos de diferentes tipos (hay que convertirlo)
print("Salario director: " + str(salario_director))

salario_jefe_area=int(input("Introduce el salario del jefe_area"))
#en python no se puede concatenar datos de diferentes tipos (hay que convertirlo)
print("Salario jefe_area: " + str(salario_jefe_area))

salario_operador=int(input("Introduce el salario del operador"))
#en python no se puede concatenar datos de diferentes tipos (hay que convertirlo)
print("Salario operador: " + str(salario_operador))

if salario_operador<salario_jefe_area<salario_director<salario_operador:
    print("el operador gana mas que todos")
else:
    print("algo esta raro en esta empresa")