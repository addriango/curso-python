class Empleado():
    def __init__(self,nombre,cargo,salario):
        self.nommbre=nombre
        self.cargo=cargo
        self.salario=salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {} $".format(self.nommbre,self.cargo,self.salario)

listaEmpleados=[
    Empleado("juan","Director",750000),
    Empleado("Ana","presidenta",850000),
    Empleado("Antonio","Administrativo",25000),
    Empleado("Sara","secretaria",27000),
    Empleado("Mario","Botones",21000),
]

salariosAltos=filter(lambda empleado: empleado.salario>50000,listaEmpleados)

for empleado_Salario in salariosAltos:
    print(empleado_Salario)
        