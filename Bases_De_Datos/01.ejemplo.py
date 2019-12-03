import sqlite3

#crear una db y abrir la conexion

miConexion=sqlite3.connect("primeraBase")

miCursor=miConexion.cursor()

#no debemos ejecutarla travez porque ya la tabla se creo
# miCursor.execute("CREATE TABLE PRODUCTOS(NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER, SECCION VARCHAR(20))")

# miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON',15,'DEPORTES')")

variosProductos=[
    ("camiseta",10,"deportes"),
    ("jarron",90,"ceramica"),
    ("camion",20,"jugueteria")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)",variosProductos)

miConexion.close()