import sqlite3 as sql

class Conexion_BD():

    def __init__(self,bd):#bd es el nombre de la base de datos
        self.conexion = sql.connect(bd)
        self.cursor = self.conexion.cursor()

    def consulta(self, consulta):
        self.cursor.execute(consulta)
    
    def commit(self):
        self.conexion.commit()

    def cerrar(self):
        self.conexion.close()

db="Supermerk.db"

class C_producto():
  def __init__(self):
    self.db= "Supermerk.db"

  def alta_producto(nombre,stock,precio,categoria):
    conexion= Conexion_BD(db)
    conexion.consulta(f"INSERT INTO Tabla_Prod(nombre, stock, precio_unitario, categoria) VALUES {nombre,stock,precio,categoria};")
    conexion.commit()
    conexion.cerrar()


  def mostrar_datos(self):
    conexion= Conexion_BD(db)
    conexion.consulta(f"Select * from Tabla_Prod")
    conexion.commit()
    datos=conexion.cursor.fetchall()
    conexion.cerrar()
    return datos

  def buscar_idProducto(self,id_producto):
    conexion= Conexion_BD(db)
    conexion.consulta(f"Select * from Tabla_Prod where id_producto={id_producto} ")
    conexion.commit()
    datos=conexion.cursor.fetchone()
    if datos != None:
      data = datos
    else:
      data= None
    #print(data)
    conexion.cerrar()
    return data
  
  #el fetchall sirve para llenar la tabla
  def buscar_idProducto_Venta(self,id_producto):
    conexion= Conexion_BD(db)
    conexion.consulta(f"Select * from Tabla_Prod where id_producto={id_producto} ")
    conexion.commit()
    datos=conexion.cursor.fetchall()
    if datos != None:
      data = datos
    else:
      data= None
    #print(data)
    conexion.cerrar()
    return data

  
  #modifica todos los campos x id_producto
  def modificar_idProducto(id_producto,nombre,stock,precio,categoria):
    conexion= Conexion_BD(db)
    conexion.consulta(f"UPDATE Tabla_Prod SET nombre= {nombre},stock= {stock},precio_unitario={precio},categoria={categoria} WHERE id_producto= {id_producto}")
    conexion.commit()
    conexion.cerrar()

  #modifica stock x id_producto
  def modificar_stock_idProducto(id_producto,stock):
    conexion= Conexion_BD(db)
    conexion.consulta(f"UPDATE Tabla_Prod SET stock = stock - {stock} WHERE id_producto = {id_producto}")
    conexion.commit()
    conexion.cerrar()
  

