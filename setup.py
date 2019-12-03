from setuptools  import setup

setup(
    name="paquete_calculos",
    version="0.0.1",
    description="Paquete de redonde y potencia",
    author="Adrian Gomez"
    author_email="adriandgomez123@gmail.com",
    url="adriangez.github.io",
    packages=["calculos","calculos.basicos"]
    
)

##ejecutar este arvhivo para crear un paquete comprimido distribuible
## pip3 install setup.py
##con esto instalamos el paquete de manera global y pude ser accedido
##desde cualquier archivo
