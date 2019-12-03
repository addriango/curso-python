def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args,**kwargs):
        #acciones adicionales que decoran
        print("Vamos a realizar un calculo: ")
        funcion_parametro(*args,**kwargs)
        print("hemos terminado el calculo")
        
    return funcion_interior

#decoraremos la funcion suma

@funcion_decoradora
def suma(num1, num2,num3):
    print(num1+num2+num3)


@funcion_decoradora
def resta(num1,num2):
    print(num1-num2)

@funcion_decoradora
def potencia(base,exponente):
    print(pow(base,exponente))

suma(10,5,5)
resta(10,3)
potencia(base=2,exponente=3)