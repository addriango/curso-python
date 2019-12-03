class Vehiculo():
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enmarcha=True
        
    def acelerar(self):
        self.acelera=True
    
    def frenar(self):
        self.frena=True
        
    def estado(self):
        print("Marca: ",self.marca,"\nModelo: ",self.modelo,
              "\nEn Marcha: ",self.enmarcha,"\nAcelerando: ",
              self.acelera,"\nFrenado: ",self.frena)

class Furgoneta(Vehiculo):

    def carga(self,cargar):
        self.cargado=cargar
        if self.cargado:
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"
    
        
#las clase moto hereda de la clase padre vehiculo
class Moto(Vehiculo):
    
    hCaballito=""
        
    def caballito(self):
        self.hCaballito="voy haciendo caballito"
        return self.hCaballito
    
    def estado(self):
        print("Marca: ",self.marca,"\nModelo: ",self.modelo,
              "\nEn Marcha: ",self.enmarcha,"\nAcelerando: ",
              self.acelera,"\nFrenado: ",self.frena,"\nCaballito: ",
              self.hCaballito)

class VElectrico(Vehiculo):
    def __init__(self,marca,modelo):
        super().__init__(marca,modelo)
        self.autonomia=100

    def cargarEnergia(self):
        self.cargando=True
    
class BiciElectrica(Vehiculo, VElectrico):
    pass       
#instancia de la clase moto
miMoto=Moto("Honda","CBR")

#metodo propio
miMoto.caballito()


#metodo heredado
miMoto.estado()        
##importante mencionar que el metodo propio tiene prioridad
##sobre el metodo heredado en caso que se llamen igual        

miFurgoneta=Furgoneta("Renault","Kangoo")
miFurgoneta.arrancar()        
miFurgoneta.estado()
print(miFurgoneta.carga(True))

##herencia multiple (una clase hereda de dos o mas clases)
##la clase con dos padres hereda el constructor de la primera
##clase padre que se pase en los parametros, en este caso
##heredara el constructor de Velectrico
# class BicicletaElectrica(Velectrico,Vehiculo):
#     pass

##como el constructor que toma es el de Velectrico
## esta instancia me dara error, ya que el contructor
## de Velectrico no recibe parametros,
##la solucion seria cambiar el orden para  que la clase
##vehiculo tenga prioridad y su constructor si recibe los dos 
##parametros mencionados

miBici=BiciElectrica("Orbea","hc1030")