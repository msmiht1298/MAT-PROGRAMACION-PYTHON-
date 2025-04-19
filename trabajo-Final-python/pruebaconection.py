import mysql.connector

conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="msdatebase")
cursor1=conexion1.cursor()
cursor1.execute("delete from articulos where codigo=1")
cursor1.execute("delete from articulos where codigo=2")
cursor1.execute("delete from articulos where codigo=3")
conexion1.commit()
cursor1.execute("select codigo, descripcion, precios from articulos")
for fila in cursor1:
    print(fila)
conexion1.close()  