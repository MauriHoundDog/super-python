import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import FPControl
from BaseDatos.Conexion_Venta import Con_VentaCliente
from BaseDatos.Conexion_Cliente import Con_Cliente


class Clase_Vista_ListaProd():
    #tomo datos del formulario para cargar a la base de datos
    #utilizare de la carpeta de BaseDatos 

    def llenarTabla(self):
        #limpia la tablaaaa
        self.tabla.delete(*self.tabla.get_children())
        #buscar por id al cliente
        try:
            id_cliente=int(self.id_cliente.get())
            conexion_cliente=Con_Cliente()
            datos=conexion_cliente.buscar_id(id_cliente)
            if datos!=None:
                datos=list(datos)
                id_cliente=datos[0]
                nombre=datos[1]
                apellido=datos[2]
                self.etiqueta_cliente.config(text="Cliente: "+nombre+" "+apellido)
                dni=datos[3]
                cel=datos[4]
                email=datos[5]
                usuario=datos[6]
                clave=datos[7]
                #mostramos lo que viene de la base de datos
                conec_Venta=Con_VentaCliente()
                datosProducto=conec_Venta.mostrar_venta_cliente(id_cliente)
                if datosProducto!=None:
                    for row in datosProducto:       
                        self.tabla.insert("","end",text=row[0], values=(row[1], row[2]))    
                else:
                    self.tabla.delete(*self.tabla.get_children())
                    messagebox.showinfo("Inactivo","Este cliente aun no ha realizado compras")
            else:
                self.tabla.delete(*self.tabla.get_children())
                self.etiqueta_cliente.config(text="Cliente: ")
                messagebox.showinfo("Inexistente","No se encuentra en la bd")
        except:
            messagebox.showerror("Error - id del Cliente","Ingrese numero entero")
            self.id_cliente.delete(0,200)
    
    def volver_panel(self):
        self.ventana.destroy()
        FPControl.Vista_PControl()
    
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Administración')
        self.ventana.geometry('800x800')
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
        titulo = tk.Label(frame_form_top, text="Listado de productos seleccionado x el usuario", font=(
            'Times', 30), fg="#666a88", bg='#fcfcfc', pady=50)
        titulo.pack(expand=tk.YES, fill=tk.BOTH)
        # end frame_form_top

        # frame_form_fill
        frame_form_fill = tk.Frame(
            frame_form, height=50,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)
        #boton volver al panel de control
        #boton salir
        btnVolver = tk.Button(frame_form_fill, text="Volver al Panel de Control", font=(
            'Times', 14), bg='#3a7ff6', bd=0, fg="#fff", command=self.volver_panel)
        btnVolver.pack(fill=tk.Y, padx=20, pady=20,anchor="e")
        btnVolver.bind("<Return>", (lambda event: self.volver_panel()))
        #nombre producto etiqueta y entry
        etiqueta_idProd = tk.Label(frame_form_fill, text="Ingrese ID del Cliente a buscar", font=(
            'Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_idProd.pack(fill=tk.X, padx=20, pady=5)
        self.id_cliente = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.id_cliente.pack(fill=tk.X, padx=20, pady=10)
        #etiqueta cliente
        self.etiqueta_cliente = tk.Label(frame_form_fill, text="Cliente: ", font=(
            'Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        self.etiqueta_cliente.pack(fill=tk.X, padx=20, pady=5)
        #boton buscar y cargar tabla (listado de productos seleccionados x el usuario) usamos la tabla venta o detalle
        btnBuscar = tk.Button(frame_form_fill, text="Buscar", font=(
            'Times', 15), bg='#3a7ff6', bd=0, fg="#fff", command=self.llenarTabla)
        btnBuscar.pack(fill=tk.X, padx=20, pady=20)
        btnBuscar.bind("<Return>", (lambda event: self.llenarTabla()))
        #preparamos la tabla
        self.tabla=ttk.Treeview(frame_form_fill,columns=("col1","col2"))
        self.tabla.column("#0",width=80,anchor="center")
        self.tabla.column("#1",anchor="center")
        self.tabla.column("#2",anchor="center")
        self.tabla.heading("#0",text="Producto",anchor="center")
        self.tabla.heading("#1",text="Precio Unitario",anchor="center")
        self.tabla.heading("#2",text="Categoria",anchor="center")
        
        self.tabla.pack()
        
        # end frame_form_fill
        self.ventana.mainloop()
#Clase_Vista_ListaProd()