class Areas():
    def areaCuadrado(lado):
        '''calcula el area de un cuadrado
        elevando al cuadrado el lado pasado por parametro'''
        return "El area de cuadrado es: " + str(lado*lado)

    
print(areaCuadrado(2))

#imprime la documentacion asociada a la funcion area cuadrado
# print(areaCuadrado.__doc__)

#la mejor desciprcion es con la funcion help
help(areaCuadrado)

'''cuando la funcion esta dentro de  una clase es decir
es un metodo lo que debemos hacer es llamar al metodo 
antecedido por la clase ej: Areas.areaCuadrado.__doc__'''