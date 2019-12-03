##la funcion filter verifica que los elementos de una lista
##cumplen una condicion, devolviendo un iterador con aquellas 
##que  la cumplen

#programa que devuellve los numeros pares de una lista de numeros
'''def numero_par(num):
    
    if num%2==0:
        return True'''
    
numeros=[17,24,7,39,8,51,100]

print(list(filter(lambda numero_par: numero_par%2==0,numeros)))
