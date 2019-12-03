class Auto():
    def __init__(self):
        self.ancho=120
        self.largo=300 
        #la variable rueda esta encapsulada
        ##ne python se encapsula con dos guines
        ##bajos antes del nobre
        self.__ruedas=4
        self.cheuqeo=True
        

    def arrancar(self):
        check=self.__chequeo()
        if check:
            print("arranacamos")
        else:
            print("algo ha ido mal en el chequeo")
    
    def estado(self):
        print(f"tienes {self.__ruedas} ruedas")
    
    def __chequeo(self):
        print("realizando chequeo interno")
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="ok"
        
        if self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="ok":
            return True
        else:
            return False

##las variables y los metodos que no estan encapsulados pueden ejecutarse
##dentro y fuera de la clase mientras que los encapsulados
##solo se ejecutan dentro de la clase


miauto = Auto()

print(miauto.estado())

miauto.arrancar()

##esto no es posible, no se puede modificar una variable encapsulada
##fuera de la clase
miauto.__ruedas=2


