#marca error porque no tenemos definida la clase vehiculo aen este archivo
import pickle

ficheroApertura=open("loscoches","rb")

miscoches=pickle.load(ficheroApertura)

ficheroApertura.close()
del (ficheroApertura)
print(miscoches)