import sqlite3 as sql
from tkinter import messagebox

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

class Con_Cliente():
  def __init__(self):
    self.db= "Supermerk.db"

  def alta_cliente(nombre,apellido, dni, cel, email,usuario, clave):
    conexion= Conexion_BD(db)
    #try:
    conexion.consulta(f"INSERT INTO Tabla_Cliente(nombre, apellido, dni, cel, email,usuario, clave) VALUES {nombre,apellido, dni, cel, email,usuario, clave};")
    #except:
     # messagebox.showerror("Ingrese otro email/usuario","ya existe un email/usuario en nuestra base de datos")

    conexion.commit()
    conexion.cerrar()
  
  def buscar_usuario(self,usuario):
    conexion= Conexion_BD(db)
    conexion.consulta(f"Select * from Tabla_Cliente where usuario={usuario} ")
    conexion.commit()
    datos=conexion.cursor.fetchone()
    if datos != None:
      data = datos
    else:
      data= None
    #print(data)
    conexion.cerrar()
    return data

  def buscar_id(self,id):
    conexion= Conexion_BD(db)
    conexion.consulta(f"Select * from Tabla_Cliente where id_cliente={id} ")
    conexion.commit()
    datos=conexion.cursor.fetchone()
    if datos != None:
      data = datos
    else:
      data= None
    #print(data)
    conexion.cerrar()
    return data

  def mostrar_datos(self):
    conexion= Conexion_BD(db)
    conexion.consulta(f"Select * from Tabla_Cliente ")
    conexion.commit()
    datos=conexion.cursor.fetchall()
    if datos != None:
      data = datos
    else:
      data= None
    #print(data)
    conexion.cerrar()
    return data




