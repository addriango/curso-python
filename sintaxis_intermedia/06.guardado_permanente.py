#vamos a crer una clase sencilla y crearemos objetos de esa clase
#luego guardaremos esos objetos en un fichero externo que permanecera
#en nuestro sistema de manera permanente hasta que dicidamos borrarlo
#o si queremos podemos reutilizarlo en otros proyectos

import pickle

class Persona:
    def __init__(self,nombre,genero,edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print(f"se ha creado una persona con el nombre {self.nombre}")

    #metodo que trae python para convertir un objeto en texto
    def __str__(self):
        return "{} {} {}".format(self.nombre,self.genero,self.edad)

class ListaPersonas:
    personas=[]
    
    def agregarPersonas(self,p):
        self.personas.append(p)
    
    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

miLista=ListaPersonas()

p=Persona("Sandra","Femenino",29)

miLista.agregarPersonas(p)

p=Persona("Antonio","Masculino",20)

miLista.agregarPersonas(p)

p=Persona("Ana","Femenino",22)

miLista.agregarPersonas(p)

miLista.mostrarPersonas()