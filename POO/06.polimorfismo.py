class Coche():
    
    def desplazamiento(self):
        print("me desplazo usando cuatro ruedas")

class Moto():
    
    def desplazamiento(self):
        print("me desplazo usando dos ruedas")
        
class Camion():
    
    def desplazamiento(self):
        print("me desplazo usando seis ruedas")
    
# mivehiculo=Moto()
# mivehiculo.desplazamiento()

# miVehiculo2=Coche()
# miVehiculo2.desplazamiento()

# miVehiculo3=Camion()
# miVehiculo3.desplazamiento()

##el polimorfismo nos permite que un objeto pueda tomar un
##valor diferente de acuerdo con el contexto
def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

mivehiculo=Camion()

desplazamientoVehiculo(mivehiculo)
