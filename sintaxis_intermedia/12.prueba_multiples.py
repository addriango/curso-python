def compruebaEmail(emailUsuario):
    
    '''
    l funcion compruebaEmail evalua un Email
    recibido en busca de la @. Si tiene una @
    es correcto.Si tiene mas de una @ es incorrecto.
    Si tiene la @ al final es incorrecto
    
    >>> compruebaEmail('juan@cursos.com')
    True
    >>> compruebaEmail('juancursos.com@')
    False
    >>> compruebaEmail('juancursos.com')
    False
    >>> compruebaEmail('juan@cursos@.com')
    False
    
    '''
    num_arrobas=emailUsuario.count('@')
    posicion=emailUsuario.find('@')
    
    if (num_arrobas!=1 or posicion==(len(emailUsuario)-1) or posicion==0):
        return False
    else:
        return True
        
import doctest

doctest.testmod()
    
    
    
    