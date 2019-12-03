##programa que evalua la distancia dela casa del estudiante al colegio
##para otorgarle una beca y si tiene mas de 2 hermanos
## y si el salario de la familia sea menor de 20000 dolares

print("progarama de becas 2020")

distancia_escuela = int(input("Introduce la distacia de tu casa hasta la escuela en km: "))
print(distancia_escuela)

numero_hermanos = int(input("Cuantos hermanos tienes?: "))
print(numero_hermanos)

salario_familia = int(input("cuanto gana tu familia en dolares?: "))
print(salario_familia)

## todas las condiciones se deben cumplir
# if distancia_escuela>40 and numero_hermanos>2 and salario_familia<=20000:
#     print("Tienes derecho a beca")
# else:
#   print("no tienes derecho a beca")

##una de las condiciones se debe cumplir
if distancia_escuela>40 or numero_hermanos>2 or salario_familia<=20000:
    print("Tienes derecho a beca")
else:
  print("no tienes derecho a beca")