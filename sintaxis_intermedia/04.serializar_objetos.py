import pickle

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

# coche1=Vehiculo("mazda","MX5")
# coche2=Vehiculo("renault","ohio")
# coche3=Vehiculo("chevrolet","xd8")

# coches=[coche1,coche2,coche3]

# fichero=open("loscoches","wb")
# pickle.dump(coches,fichero)
# fichero.close()
# del (fichero)


#si leemos la serializacion desde este mismo archivo va a funcionar
#porque tenemos definida la clase pero si hacemos la misma lectura 
#desde otro archivo donde no esta defina la clase marcara error porque
#no sabe que es un objeto vehiculo

ficheroApertura=open("loscoches","rb")

miscoches=pickle.load(ficheroApertura)

ficheroApertura.close()
del (ficheroApertura)
for coche in miscoches:
    print(coche.estado())