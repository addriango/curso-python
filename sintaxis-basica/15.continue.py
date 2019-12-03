## la palabra clave "continue" ignora todo lo que esta debajo 
## de el en la iteracion donde se cumple la condicion
for letra in "python":
    if letra =="h":
        continue
    print(f"viendo la letra {letra}")

nombre = "Adrian David Gomez Rivera"

print(len(nombre))

contador_caracteres = 0
for i in nombre:
    if i == " ":
        continue
    contador_caracteres+=1

print(contador_caracteres)
        