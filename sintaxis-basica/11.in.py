print("Asignatutas opcionales 2020")
print("Informatica grafica - Pruebas de softwre - usabilidad y accesibilidad")
opcion = input("Escribe la asigtatura que quieres ver: ")
asignatura = opcion.lower()

lista = ("informatica grafica","pruebas de software","usabilidad y accesibilidad")
## el operador in se utiliza para saber si un dato esta dentro de una lista / tupla
if asignatura in lista:
    print("Asignatura elegida " + asignatura)
else:
    print("La asignatur elegida no esta comtemplada")