## son un conjunto de lineas de codigo que realizar una tarea especifica
## pueden tener parametros y devolver un resultado
## tambien se les llama metodos si estan dentro de una clase(veremos mas adelante)


##funcion sin parametros/argumentos
def saludar():
    return print("hola como estas")

##funciones predefinidas / ya las trae el lenguaje como la funcion print
## que imprime en pantalla un dato

print("hola mundo")

##funciones propias
def sumar_tres_numeros(a,b,c):
    resultado = a + b + c
    return resultado

    
sumar_tres_numeros(1,2,3) #6

