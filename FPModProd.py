import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import FPControl
from BaseDatos.Conexion_Producto import C_producto
import Clase_Producto

class Clase_Vista_Mod_Prod():
    #tomo datos del formulario para cargar a la base de datos
    #utilizare de la carpeta de BaseDatos la clase Conexion_Producto
    
    def modificar_producto(self):
        #busco el producto x id
        try:
            id_producto=int(self.id_prod.get())
            try:
                stock_prod=int(self.cant_prod.get())
                try:
                    precio_prod=float(self.precio_prod.get())
                    nombre_prod="'"+self.nombre_prod.get()+"'"
                    categoria_prod="'"+self.cat_prod.get()+"'"
                    Producto=Clase_Producto.Producto(id_producto,nombre_prod,stock_prod,precio_prod,categoria_prod)
                    Producto.update_producto()
                    messagebox.showinfo("Exitoso","se modifico correctamente")
                    self.ventana.destroy()
                    FPControl.Vista_PControl()
                except:
                    messagebox.showerror("Error - Precio","Ingrese numero real (con . para parte decimal)")
                    self.precio_prod.delete(0,200)
            except:
                messagebox.showerror("Error - stock","Ingrese numero entero")
                self.cant_prod.delete(0,200)
                
        except:
            messagebox.showerror("Error - id del Producto","Ingrese numero entero")
            self.id_prod.delete(0,200)
        

    def buscar_producto(self):
        try:
            id_producto_input=int(self.id_prod.get())
            con_Producto=C_producto()
            datos=con_Producto.buscar_idProducto(id_producto_input)
            if datos!=None:
                messagebox.showinfo("Producto encontrado","Puede modificar los datos")
                #vamos habilitar y cargar los label con datos de la bd
                self.nombre_prod["state"]="normal"
                self.cant_prod["state"]="normal"
                self.precio_prod["state"]="normal"
                self.cat_prod["state"]="normal"
                self.btnAceptar["state"]="normal"
                #cargamos los datos en variables
                nombre_producto=datos[1]
                stock_producto=datos[2]
                precio_producto=datos[3]
                categoria_producto=datos[4]
                #limpiamos los entry
                self.nombre_prod.delete(0,200)
                self.cant_prod.delete(0,200)
                self.precio_prod.delete(0,200)
                self.cat_prod.delete(0,200)
                self.nombre_prod.insert(0,nombre_producto)
                self.cant_prod.insert(0,str(stock_producto))
                self.precio_prod.insert(0,str(precio_producto))
                self.cat_prod.insert(0,categoria_producto)
            else:
                self.nombre_prod["state"]="disabled"
                self.cant_prod["state"]="disabled"
                self.precio_prod["state"]="disabled"
                self.cat_prod["state"]="disabled"
                self.btnAceptar["state"]="disabled"
                messagebox.showwarning("No se encontro","Producto inexistente")
        except:
            messagebox.showerror("Error - id del Producto","Ingrese numero entero")
            self.id_prod.delete(0,200)
            
    
    def volver_btn(self):
        self.ventana.destroy()
        FPControl.Vista_PControl()

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Administración')
        self.ventana.geometry('800x800')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)

        nombre_producto=""
        # frame_form
        frame_form = tk.Frame(self.ventana, bd=0,
                              relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)

        # frame_form_top
        frame_form_top = tk.Frame(
            frame_form, height=50, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="Modificar Producto", font=(
            'Times', 30), fg="#666a88", bg='#fcfcfc', pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)
        # end frame_form_top

        # frame_form_fill
        frame_form_fill = tk.Frame(
            frame_form, height=50,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        #boton salir
        btnVolver = tk.Button(frame_form_fill, text="Volver al Panel de Control", font=(
            'Times', 14), bg='#3a7ff6', bd=0, fg="#fff", command=self.volver_btn)
        btnVolver.pack(fill=tk.Y, padx=20, pady=20,anchor="e")
        btnVolver.bind("<Return>", (lambda event: self.volver_btn()))    

        #id producto etiqueta y entry
        etiqueta_id_prod = tk.Label(frame_form_fill, text="Ingrese ID del producto", font=(
            'Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_id_prod.pack(fill=tk.X, padx=20, pady=5)
        self.id_prod = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.id_prod.pack(fill=tk.X, padx=20, pady=10)

        #boton buscar_idProducto
        btnBuscar = tk.Button(frame_form_fill, text="Buscar Producto", font=(
            'Times', 15), bg='#3a7ff6', bd=0, fg="#fff", command=self.buscar_producto)
        btnBuscar.pack(fill=tk.Y, padx=20, pady=20,anchor="w")
        btnBuscar.bind("<Return>", (lambda event: self.buscar_producto()))

        #nombre producto etiqueta y entry
        etiqueta_nombre_prod = tk.Label(frame_form_fill, text="Nombre del producto", font=(
            'Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_nombre_prod.pack(fill=tk.X, padx=20, pady=5)
        self.nombre_prod = ttk.Entry(frame_form_fill, font=('Times', 14),state="disabled")
        self.nombre_prod.pack(fill=tk.X, padx=20, pady=10)

        #precio producto etiqueta y entry
        etiqueta_precio_prod = tk.Label(frame_form_fill, text="Precio $", font=(
            'Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_precio_prod.pack(fill=tk.X, padx=20, pady=5)
        self.precio_prod = ttk.Entry(frame_form_fill, font=('Times', 14),state="disabled")
        self.precio_prod.pack(fill=tk.X, padx=20, pady=10)

        #cantidad producto etiqueta y entry
        etiqueta_cant_prod = tk.Label(frame_form_fill, text="Cantidad", font=(
            'Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_cant_prod.pack(fill=tk.X, padx=20, pady=5)
        self.cant_prod = ttk.Entry(frame_form_fill, font=('Times', 14),state="disabled")
        self.cant_prod.pack(fill=tk.X, padx=20, pady=10)

        #categoria producto etiqueta y entry
        etiqueta_cat_prod = tk.Label(frame_form_fill, text="Categoria", font=(
            'Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_cat_prod.pack(fill=tk.X, padx=20, pady=5)
        self.cat_prod = ttk.Entry(frame_form_fill, font=('Times', 14),state="disabled")
        self.cat_prod.pack(fill=tk.X, padx=20, pady=10)

        #boton aceptar
        self.btnAceptar = tk.Button(frame_form_fill, text="Aceptar/Modificar", font=(
            'Times', 15), bg='#3a7ff6', bd=0, fg="#fff", command=self.modificar_producto,state="disabled")
        self.btnAceptar.pack(fill=tk.X, padx=20, pady=20)
        self.btnAceptar.bind("<Return>", (lambda event: self.modificar_producto()))

        
        
        # end frame_form_fill
        self.ventana.mainloop()
#Clase_Vista_Mod_Prod()