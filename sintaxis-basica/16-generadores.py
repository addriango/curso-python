##los generadores extraen valores de una funcion y se almacenan en objetos
## iterables (que se pueden recorrer)

##funcion tradicional que  cree numeros pares

def generaPares(limite):
    num=1
    miLista=[]
    while num<limite:
        miLista.append(num*2)
        num+=1
    return miLista


print(generaPares(10))

##generadores

def genPares(limite):
    num = 1
    while num<limite:
        yield num*2
        num+=1

devuelvePares = genPares(11)
for i in devuelvePares:
    print(i)    