import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import FPControl
import Clase_Producto

class Clase_Vista_AltaProd():
    #tomo datos del formulario para cargar a la base de datos
    #utilizare de la carpeta de BaseDatos la clase Conexion_Producto
    def alta_producto(self):

        nombre_producto=self.nom_prod.get()
        try:
            stock=int(self.cant_prod.get())
            try:
                precio=float(self.precio_prod.get())
                categoria=self.cat_prod.get()
                if nombre_producto!= "" and stock!="" and precio !="" and categoria!="":
                        id_producto=""
                        Produc=Clase_Producto.Producto(id_producto,nombre_producto,stock,precio,categoria)
                        Produc.cargar_producto()
                        messagebox.showinfo("Nuevo Producto","se cargo a la BD")
                        self.ventana.destroy()
                        FPControl.Vista_PControl()
                else:
                    messagebox.showinfo("Error","Complete todos los campos")
            except:
                messagebox.showinfo("Error - Precio","ingrese numero real(con . para parte decimal")
                self.precio_prod.delete(0,200)
        except:
                messagebox.showinfo("Error - Stock","ingrese numero entero")
                self.cant_prod.delete(0,200)
    
    def volver_btn(self):
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
        title = tk.Label(frame_form_top, text="Cargar Producto", font=(
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

        #nombre producto etiqueta y entry
        etiqueta_nom_prod = tk.Label(frame_form_fill, text="Nombre Producto", font=(
            'Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_nom_prod.pack(fill=tk.X, padx=20, pady=5)
        self.nom_prod = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.nom_prod.pack(fill=tk.X, padx=20, pady=10)

        #cantidad producto etiqueta y entry
        etiqueta_cant_prod = tk.Label(frame_form_fill, text="Stock", font=(
            'Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_cant_prod.pack(fill=tk.X, padx=20, pady=5)
        self.cant_prod = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.cant_prod.pack(fill=tk.X, padx=20, pady=10)

        #precio producto etiqueta y entry
        etiqueta_precio_prod = tk.Label(frame_form_fill, text="Precio Unitario $", font=(
            'Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_precio_prod.pack(fill=tk.X, padx=20, pady=5)
        self.precio_prod = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.precio_prod.pack(fill=tk.X, padx=20, pady=10)
        
        #categoria producto etiqueta y entry
        etiqueta_cat_prod = tk.Label(frame_form_fill, text="Categoria", font=(
            'Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_cat_prod.pack(fill=tk.X, padx=20, pady=5)
        self.cat_prod = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.cat_prod.pack(fill=tk.X, padx=20, pady=10)

        btnAceptar = tk.Button(frame_form_fill, text="Aceptar/Cargar", font=(
            'Times', 15), bg='#3a7ff6', bd=0, fg="#fff", command=self.alta_producto)
        btnAceptar.pack(fill=tk.X, padx=20, pady=20)
        btnAceptar.bind("<Return>", (lambda event: self.alta_producto()))

        
        
        # end frame_form_fill
        self.ventana.mainloop()
#Clase_Vista_AltaProd()