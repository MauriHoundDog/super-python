import tkinter as tk
from tkinter import ttk
import FPAltaProd,FPDatosVenta,FPListProd,FPModProd,FLogin

class Vista_PControl():

    def volver_panel_btn1(self):
        self.ventana.destroy()
        FPAltaProd.Clase_Vista_AltaProd()

    def volver_panel_btn2(self):
        self.ventana.destroy()
        FPModProd.Clase_Vista_Mod_Prod()

    def volver_panel_btn3(self):
        self.ventana.destroy()
        FPDatosVenta.Clase_Vista_DatosVenta()

    def volver_panel_btn4(self):
        self.ventana.destroy()
        FPListProd.Clase_Vista_ListaProd()

    def volver_panel_btn5(self):
        self.ventana.destroy()
        FLogin.Clase_Vista_Login()
    
    

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
        title = tk.Label(frame_form_top, text="Panel de Control", font=(
            'Times', 30), fg="#666a88", bg='#fcfcfc', pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        #boton salir
        btnSalir = tk.Button(frame_form_top, text="Salir", font=(
            'Times', 15), bg='#3a7ff6', bd=0, fg="#fff",command=self.volver_panel_btn5)
        btnSalir.pack(fill=tk.X, padx=20, pady=20)
        btnSalir.bind("<Return>", (lambda event: self.volver_panel_btn5()))
        # end frame_form_top

        # frame_form_fill
        frame_form_fill = tk.Frame(
            frame_form, height=50,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)
       
        #boton alta producto
        btnAltaProd = tk.Button(frame_form_fill, text="Cargar Productos", font=(
            'Times', 15), bg='#3a7ff6', bd=0, fg="#fff",command=self.volver_panel_btn1)
        btnAltaProd.pack(fill=tk.X, padx=20, pady=20)
        btnAltaProd.bind("<Return>", (lambda event: self.volver_panel_btn1()))
        #boton modificar producto
        btnModProd = tk.Button(frame_form_fill, text="Modificar Productos", font=(
            'Times', 15), bg='#3a7ff6', bd=0, fg="#fff", command=self.volver_panel_btn2)
        btnModProd.pack(fill=tk.X, padx=20, pady=20)
        btnModProd.bind("<Return>", (lambda event: self.volver_panel_btn2()))
        #boton ver todos los usuarios que realizaron compras
        btnVerUsu = tk.Button(frame_form_fill, text="Ver todos clientes que realizaron compras", font=(
            'Times', 15), bg='#3a7ff6', bd=0, fg="#fff", command=self.volver_panel_btn3)
        btnVerUsu.pack(fill=tk.X, padx=20, pady=20)
        btnVerUsu.bind("<Return>", (lambda event: self.volver_panel_btn3()))
        #boton ver listado de productos seleccionado x el usuario
        btnVerProd = tk.Button(frame_form_fill, text="Ver productos seleccionado por el usuario", font=(
            'Times', 15), bg='#3a7ff6', bd=0, fg="#fff", command=self.volver_panel_btn4)
        btnVerProd.pack(fill=tk.X, padx=20, pady=20)
        btnVerProd.bind("<Return>", (lambda event: self.volver_panel_btn4()))

        
        # end frame_form_fill
        self.ventana.mainloop()

#Vista_PControl()