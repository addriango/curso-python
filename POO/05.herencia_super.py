class Persona():
    def __init__(self,nombre,edad,residencia):
        self.nombre=nombre
        self.edad=edad
        self.residencia=residencia

    def descripcion(self):
        print(f"{self.nombre}, {self.edad}, {self.residencia}")
        
class Empleado(Persona):
    def __init__(self,salario,antiguedad,nombre_empleado,edad_empleado,
                 residencia_empleado):
        super().__init__(nombre_empleado,edad_empleado,residencia_empleado)
        self.salario=salario
        self.antiguedad=antiguedad
    
    def descripcion(self):
        super().descripcion()
        print(f"{self.salario}, {self.antiguedad}")
        
# Antonio=Empleado(1500,15,"manuel",45,"Colombia")   
Antonio=Persona("manuel",45,"Colombia")   

Antonio.descripcion() 

##el metodo isinstance nos permite saber de que clases es inastancia un onjeto
print(isinstance(Antonio,Empleado)) #devuelve true si manuel hace parte de la clase empleado
print(isinstance(Antonio,Persona)) #devuelve true si hace parte de la clase persona