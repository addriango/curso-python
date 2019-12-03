#la funcion map aplica una funcion a cada elemento de una lista iterable
# devolviendo una lista con los resultados

class Empleado():
    def __init__(self,nombre,cargo,salario):
        self.nommbre=nombre
        self.cargo=cargo
        self.salario=salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {} $".format(self.nommbre,self.cargo,self.salario)

listaEmpleados=[
    Empleado("juan","Director",6700),
    Empleado("Ana","presidenta",7500),
    Empleado("Antonio","Administrativo",2100),
    Empleado("Sara","secretaria",2150),
    Empleado("Mario","Botones",1800),
]

def calculo_comision(empleado):
    #aplicara la comision solo  lso que ganen meos de 3000$
    if empleado.salario<3000:
        empleado.salario*=1.03
    return empleado

listaEmpleadosconComision=map(calculo_comision,listaEmpleados)
for empleado in listaEmpleadosconComision:
    print(empleado)