midiccionario = {
  "pais":"capital",
  "colombia":"bogota",
  "argentina":"buenos aires",
  "francia":"paris",
  "españa":"madrid"
}

print(midiccionario.keys()) #imprime todas las claves
print(midiccionario.values()) #imprimi todos los valores

midiccionario["Italia"]="lisboa" #añade un nuevo elemento al objecto

midiccionario["Italia"]="Roma" #editar un valor del objecto

del midiccionario["argentina"]="buenos aires" #elimina el elemento

print(midiccionario["colombia"]) ##cual es el valor asignado a esa clave