import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import FLogin
import Clase_Cliente

class Clase_Vista_Registrar():


    
    #tomo datos del formulario para cargar a la base de datos
    #utilizare de la carpeta de BaseDatos la clase Conexion_Cliente
    def alta_cliente(self):
        #aqui ahi que usar try y except

        nombre=self.nombre_cliente.get()
        apellido=self.apellido_cliente.get()
        dni=self.dni_cliente.get()
        cel=self.cel_cliente.get()
        email=self.email_cliente.get()
        usuario=self.usuario_cliente.get()
        clave=self.pass_cliente.get()
        id_cliente=""
        if nombre!="" and apellido!="" and dni!="" and cel!="" and email!="" and usuario!="" and clave!="":
            Cliente=Clase_Cliente.Cliente(id_cliente,nombre,apellido,dni,cel,email,usuario,clave)
            try:
                Cliente.cargar_cliente()
                messagebox.showinfo("Alta Cliente","se cargo con correctamente a la BD")
                self.ventana.destroy()
                FLogin.Clase_Vista_Login()
            except:
                messagebox.showerror("Ingrese otro email/usuario","ya existe un email/usuario en nuestra base de datos")
                self.email_cliente.delete(0,200)
                self.usuario_cliente.delete(0,200)
        else:
            messagebox.showerror("Error","Complete todos los campos")


        

    def volver_btn(self):
        self.ventana.destroy()
        FLogin.Clase_Vista_Login()

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Alta de Cliente')
        self.ventana.geometry('800x900')
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
        titulo = tk.Label(frame_form_top, text="Registracion de cliente", font=(
            'Times', 30), fg="#666a88", bg='#fcfcfc', pady=50)
        titulo.pack(expand=tk.YES, fill=tk.BOTH)
        
        # end frame_form_top

        # frame_form_fill
        frame_form_fill = tk.Frame(
            frame_form, height=50,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        #boton salir
        btnVolver = tk.Button(frame_form_fill, text="SALIR", font=(
            'Times', 14), bg='#3a7ff6', bd=0, fg="#fff", command=self.volver_btn)
        btnVolver.pack(fill=tk.Y, padx=20, pady=20,anchor="e")
        btnVolver.bind("<Return>", (lambda event: self.volver_btn()))

        #Nombre cliente etiqueta y entry
        etiqueta_nombre = tk.Label(frame_form_fill, text="NOMBRE", font=(
            'Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_nombre.pack(fill=tk.X, padx=20, pady=5)
        self.nombre_cliente = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.nombre_cliente.pack(fill=tk.X, padx=20, pady=10)

        #Apellido cliente etiqueta y entry
        etiqueta_apellido = tk.Label(frame_form_fill, text="APELLIDO", font=(
            'Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_apellido.pack(fill=tk.X, padx=20, pady=5)
        self.apellido_cliente = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.apellido_cliente.pack(fill=tk.X, padx=20, pady=10)


        #dni cliente etiqueta y entry
        etiqueta_dni= tk.Label(frame_form_fill, text="DNI/CUIT", font=(
            'Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_dni.pack(fill=tk.X, padx=20, pady=5)
        self.dni_cliente = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.dni_cliente.pack(fill=tk.X, padx=20, pady=10)

        #cel cliente etiqueta y entry
        etiqueta_cel= tk.Label(frame_form_fill, text="CELULAR", font=(
            'Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_cel.pack(fill=tk.X, padx=20, pady=5)
        self.cel_cliente = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.cel_cliente.pack(fill=tk.X, padx=20, pady=10)

        #email cliente etiqueta y entry
        etiqueta_email= tk.Label(frame_form_fill, text="EMAIL", font=(
            'Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_email.pack(fill=tk.X, padx=20, pady=5)
        self.email_cliente = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.email_cliente.pack(fill=tk.X, padx=20, pady=10)

        #usuario cliente etiqueta y entry
        etiqueta_usuario= tk.Label(frame_form_fill, text="USUARIO", font=(
            'Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20, pady=5)
        self.usuario_cliente = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.usuario_cliente.pack(fill=tk.X, padx=20, pady=10)

        #pass cliente etiqueta y entry
        etiqueta_pass= tk.Label(frame_form_fill, text="PASSWORD", font=(
            'Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_pass.pack(fill=tk.X, padx=20, pady=5)
        self.pass_cliente = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.pass_cliente.pack(fill=tk.X, padx=20, pady=10)

        #boton aceptar DAR ALTA
        btnAceptar = tk.Button(frame_form_fill, text="Registrarse", font=(
            'Times', 14), bg='#3a7ff6', bd=0, fg="#fff", command=self.alta_cliente)
        btnAceptar.pack(fill=tk.X, padx=20, pady=20)
        btnAceptar.bind("<Return>", (lambda event: self.alta_cliente()))

        
        # end frame_form_fill
        self.ventana.mainloop()
#Clase_Vista_Registrar()
