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

class Con_VentaCliente():
    def __init__(self):
        self.db= "Supermerk.db"

    def mostrar_datos(self):
        conexion= Conexion_BD(db)
        conexion.consulta(f"select id_venta,nombre,apellido,dni,email from Tabla_Venta inner join Tabla_Cliente where Tabla_Venta.id_cliente=Tabla_Cliente.id_cliente")
        conexion.commit()
        datos=conexion.cursor.fetchall()
        #print(datos)
        conexion.cerrar()
        return datos

    def mostrar_venta_cliente(self,id_cliente):
        conexion= Conexion_BD(db)
        conexion.consulta(f"SELECT Tabla_Prod.nombre, Tabla_Prod.precio_unitario ,Tabla_Prod.categoria FROM Tabla_Prod where Tabla_Prod.id_producto in (SELECT Tabla_Venta.id_producto from Tabla_Venta WHERE Tabla_Venta.id_cliente ={id_cliente})")
        conexion.commit()
        datos=conexion.cursor.fetchall()
        if datos != None:
            data = datos
        else:
            data= None
        if datos==[]:
            data=None
        #print(data)
        conexion.cerrar()
        return data

    def alta_venta(self,id_cliente,id_producto,fecha):
        conexion= Conexion_BD(db)
        conexion.consulta(f"INSERT INTO Tabla_Venta(id_cliente,id_producto,fecha) VALUES {id_cliente,id_producto,fecha};")
        conexion.commit()
        conexion.cerrar()

#conec=Con_VentaCliente()
#conec.mostrar_venta_cliente(1)