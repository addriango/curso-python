def areaTriangulo(base,altura):
    '''
    calcula el area de un triangulo teniendo su base y su altura
    >>> areaTriangulo(3,6)
    9.0
    >>> areaTriangulo(4,5)
    10.0
    >>> areaTriangulo(9,3)
    13.5
    '''
    return (base*altura)/2

import doctest

doctest.testmod()

'''si ejecuto el programa y el en el test el resultado
esperado es diferente del que realmente obtuvo
me marcara error'''