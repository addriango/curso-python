# son funciones que añaden funcionalidades a otras funciones
#esta formado por tres funciones (A,B,C)
# donde A recibe como parametro a B para devolver C

def funcion_decoradora(funcion_parametro):
    def funcion_interior():
        #acciones adicionales que decoran
        print("Vamos a realizar un calculo: ")
        funcion_parametro()
        print("hemos terminado el calculo")
        
    return funcion_interior

#decoraremos la funcion suma

@funcion_decoradora
def suma():
    print(10+10)


@funcion_decoradora
def resta():
    print(30-20)

suma()
resta()