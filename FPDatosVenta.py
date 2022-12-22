import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import FPControl
from BaseDatos.Conexion_Venta import Con_VentaCliente

class Clase_Vista_DatosVenta():
    #tomo datos del formulario para cargar a la base de datos
    #utilizare de la carpeta de BaseDatos la clase Conexion_Producto
    def mostrar_usuarios_compra(self):
        messagebox.showinfo("Cargando","se cargo correctamente")
    
    def volver_panel(self):
        self.ventana.destroy()
        FPControl.Vista_PControl()

    def llenarTabla(self):
        Conexion_Venta=Con_VentaCliente()
        datos=Conexion_Venta.mostrar_datos()
        for row in datos:
            self.tabla.insert("","end",text=row[0], values=(row[1],row[2],row[3],row[4]))    

    
    
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Administración')
        self.ventana.geometry('1200x800')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)

        # frame_form
        frame_form = tk.Frame(self.ventana, bd=0,
                              relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)

        # frame_form_top
        frame_form_top = tk.Frame(
            frame_form, height=50, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top", fill=tk.X)
        titulo = tk.Label(frame_form_top, text="Usuarios que realizaron una compra", font=(
            'Times', 30), fg="#666a88", bg='#fcfcfc', pady=50)
        titulo.pack(expand=tk.YES, fill=tk.BOTH)
        # end frame_form_top

        # frame_form_fill
        frame_form_fill = tk.Frame(
            frame_form, height=50,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)
        #boton salir
        btnVolver = tk.Button(frame_form_fill, text="Volver al Panel de Control", font=(
            'Times', 14), bg='#3a7ff6', bd=0, fg="#fff", command=self.volver_panel)
        btnVolver.pack(fill=tk.Y, padx=20, pady=20,anchor="e")
        btnVolver.bind("<Return>", (lambda event: self.volver_panel()))
        #nombre producto etiqueta y entry
        etiqueta_datos_venta = tk.Label(frame_form_fill, text="Datos de Venta", font=(
            'Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_datos_venta.pack(fill=tk.X, padx=20, pady=5)

        #botn cargar
        btnCargar = tk.Button(frame_form_fill, text="Cargar", font=(
            'Times', 15), bg='#3a7ff6', bd=0, fg="#fff", command=self.llenarTabla)
        btnCargar.pack(fill=tk.X, padx=20, pady=20)
        btnCargar.bind("<Return>", (lambda event: self.llenarTabla()))

    
        #falta un grid o un contenedor para cargar los datos
        self.tabla=ttk.Treeview(frame_form_fill,columns=("col1","col2","col3","col4"))

        self.tabla.column("#0",width=80,anchor="center")
        self.tabla.column("#1",anchor="center")
        self.tabla.column("#2",anchor="center")
        self.tabla.column("#3",anchor="center")
        self.tabla.column("#4",anchor="center")

        self.tabla.heading("#0",text="ID Venta",anchor="center")
        self.tabla.heading("#1",text="Nombre",anchor="center")
        self.tabla.heading("#2",text="Apellido",anchor="center")
        self.tabla.heading("#3",text="DNI",anchor="center")
        self.tabla.heading("#4",text="Email",anchor="center")
        self.tabla.pack()


        
        # end frame_form_fill
        self.ventana.mainloop()

    

#Clase_Vista_DatosVenta()