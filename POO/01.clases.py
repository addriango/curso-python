#las clases son un conjunto de caracteristicas comunes de un grupo de objetos
class Automovil():
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enMarcha = False
    
    def arrancar(self):
        self.enMarcha = True
        return "arranco!!!"
    def estado(self):
        if(self.enMarcha == True):
            return "el auto esta en marcha"
        else:
            return "el auto esta detenido"

miAuto = Automovil()

print(miAuto.ruedas)
print(miAuto.estado())
print(miAuto.arrancar())
print(miAuto.estado())