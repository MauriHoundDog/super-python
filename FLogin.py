import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import FAltaCliente,FPControl
import Clase_Cliente
import FVenta
from BaseDatos.Conexion_Cliente import Con_Cliente


class Clase_Vista_Login():
        
    def verificar(self):
        #buscar por usuario si se encuentra registrado en la base de datos, y tomar, obtener la clave para luego comparar con lo que ingreso el usuario
        usuario="'"+self.usuario.get()+"'"
        Conec_Cliente=Con_Cliente()
        datos=Conec_Cliente.buscar_usuario(usuario)
        if datos!= None:
            datos=list(datos)
            id_cliente=datos[0]
            nombre=datos[1]
            apellido=datos[2]
            dni=datos[3]
            cel=datos[4]
            email=datos[5]
            usuario=datos[6]
            clave=datos[7]
            if usuario== "admin":
                if self.password.get() == clave:
                    messagebox.showinfo("Acceso Permitido","Bienvenido Administrador "+nombre)
                    self.ventana.destroy()
                    FPControl.Vista_PControl()
                else:
                    messagebox.showerror("Error","Contraseña Incorrecta")
            else:
                if self.password.get() == clave:
                    messagebox.showinfo("Acceso Permitido","Bienvenido "+nombre)
                    Cliente=Clase_Cliente.Cliente(id_cliente,nombre,apellido,dni,cel,email,usuario,clave)
                    self.ventana.destroy()
                    FVenta.Clase_Vista_Venta(Cliente)
                else:
                    messagebox.showerror("Error","Contraseña Incorrecta")
        else:
            messagebox.showerror("Inexistente","Usuario Incorrecto")
        


    def fun_btnRegistrar(self):
        self.ventana.destroy()
        FAltaCliente.Clase_Vista_Registrar()
   
    
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('---SUPERMERK2---')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)

        icono = tk.PhotoImage(file="icono16.png")
        self.ventana.iconphoto(True, icono)
        # frame_form
        frame_form = tk.Frame(self.ventana, bd=0,
                              relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)

        # frame_form_top
        frame_form_top = tk.Frame(
            frame_form, height=50, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="Inicio de sesion", font=(
            'Times', 30), fg="#666a88", bg='#fcfcfc', pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)
        # end frame_form_top

        # frame_form_fill
        frame_form_fill = tk.Frame(
            frame_form, height=50,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        etiqueta_usuario = tk.Label(frame_form_fill, text="Usuario", font=(
            'Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20, pady=5)
        self.usuario = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.usuario.pack(fill=tk.X, padx=20, pady=10)

        etiqueta_password = tk.Label(frame_form_fill, text="Contraseña", font=(
            'Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20, pady=5)
        self.password = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.password.pack(fill=tk.X, padx=20, pady=10)
        self.password.config(show="*")

        btnSesion = tk.Button(frame_form_fill, text="Entrar", font=(
            'Times', 15), bg='#3a7ff6', bd=0, fg="#fff", command=self.verificar)
        btnSesion.pack(fill=tk.X, padx=20, pady=20)
        btnSesion.bind("<Return>", (lambda event: self.verificar()))
        
        
        btnRegistrar = tk.Button(frame_form_fill, text="Registrar usuario", font=(
            'Times', 15), bg='#fcfcfc', bd=0, fg="#3a7ff6", command=self.fun_btnRegistrar)
        btnRegistrar.pack(fill=tk.X, padx=20, pady=20)
        btnRegistrar.bind("<Return>", (lambda event: self.fun_btnRegistrar()))

        
        
        # end frame_form_fill
        self.ventana.mainloop()
#Clase_Vista_Login()