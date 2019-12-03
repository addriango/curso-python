## las tuplas son listas que no modemos modificar
## ni añadir ni eleminar ni editar items
## si permiten  ver si un elemento esta en una tupla


miTupla = ("fredy","leon","mariana")

#convertir una tupla en lista
milista = list(miTupla)

#convertir una tupla en lista
milista = tuple(milista)

print("fredy" in miTupla) #devuelve True si el elemento esta en la tupla

print(miTupla.count("leon")9 #el metodo coun sirve pra saber cuantas veces esta un elemtno en una tupla
len(miTupla) # cuantos elementos tiene una tupla 0 lista
print(len(milista))

nuevatupla = ("frank",12,3,1995)
nombre, dia, mes, anio = nuevatupla #asigna cada valor de la tupla a cada variable respectivamente

