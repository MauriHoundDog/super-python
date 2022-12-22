import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import FLogin
from BaseDatos.Conexion_Producto import C_producto
import Clase_Producto
from datetime import datetime
from BaseDatos.Conexion_Venta import Con_VentaCliente


class Clase_Vista_Venta():
    #tomo datos del formulario para cargar a la base de datos
    #utilizare de la carpeta de BaseDatos la clase Conexion_Producto
    Producto=C_producto()

    #def mostrar_usuarios_compra(self):
     #   messagebox.showinfo("Cargando","se cargo correctamente")
    
    def volver_login(self):
        self.ventana.destroy()
        FLogin.Clase_Vista_Login()

    def llenarTabla(self):
        #limpia la tablaaaa
        self.tabla.delete(*self.tabla.get_children())
        datos=self.Producto.mostrar_datos()
        for row in datos:
            #print(row)
            self.tabla.insert("","end",text=row[0], values=(row[1],row[2],row[3],row[4]))
        self.id_prod["state"]="normal"
        self.cantidad["state"]="normal"
        self.btnCargarCompra["state"]="normal"
        
    
    def cargarCarrito(self):
        try:
            #buscar por id el producto deseado
            id_producto_input=int(self.id_prod.get())
            stock_input=int(self.cantidad.get())
            subtotal=0
            con_Producto=C_producto()
            datos=con_Producto.buscar_idProducto(id_producto_input)
            datos1=con_Producto.buscar_idProducto_Venta(id_producto_input)

            if datos!=None:
                if int(datos[2])!=0:
                    id_producto=datos[0]
                    nombre_producto=datos[1]
                    stock_producto=datos[2]
                    precio_producto=datos[3]
                    categoria_producto=datos[4]
                    #print(datos)#puedo guardar y armar lista de datos
                    Producto=Clase_Producto.Producto(id_producto,nombre_producto,int(stock_producto),float(precio_producto),categoria_producto)
                    #vamos a verificar la cantidad de productos cargados en la lista de productos
                    
                    if stock_input<=30:
                        if stock_input<=Producto.stock:
                            self.suma+=stock_input
                            if self.suma<=30:
                                #agrego producto a la lista de productos
                                Producto.stock=stock_input
                                self.Lista_Productos.append(Producto)
                                messagebox.showinfo("Carrito","se agrego al carrito")
                                self.btnComprar["state"]="normal"
                                subtotal=stock_input*Producto.precio
                                self.total+=subtotal
                                self.etiquetaTotal.config(text="Total: $"+str(self.total))
                                #muestro lista en la tabla.triveew
                                if datos1!=None:
                                    for row in datos1:
                                        #falta mostar subtotal en la tabla y total en la etiqueta
                                        self.tablaCarrito.insert("","end",text=row[0], values=(row[1],stock_input,row[3], subtotal))
                                        self.stock_carrito+=stock_input
                            else:
                                messagebox.showinfo("Exedente de productos","Hasta 30 articulos")
                        else:
                            messagebox.showinfo("solo hay: "+str(Producto.stock),"No hay stock suficiente para este producto")
                    else:
                        messagebox.showinfo("Excedente de productos","Hasta 30 articulos")
                else:
                    messagebox.showinfo("Elija otro producto","No hay stock para este producto")
            else:
                messagebox.showwarning("No se encontro","Producto inexistente")
        except:
            messagebox.showerror("Error Datos","Ingrese numero entero")
            self.id_prod.delete(0,200)
            self.cantidad.delete(0,200)

    def aceptarCompra(self):
        try:
            #agrego a la base de datos de tabla_venta la lista de productos
            fecha = str(datetime.now())
            id_cliente=self.id_cli
            for producto in self.Lista_Productos:
                conexionVenta=Con_VentaCliente()
                conexionVenta.alta_venta(id_cliente,producto.id_prod,fecha)    
            #modifico la base de datos de Producto - Stock
            conexion_producto=C_producto()
            for producto in self.Lista_Productos:
                #modificar stock de la tabla producto por id
                #conexion_producto.modificar_stock_idProducto(int(producto.id_prod),int(producto.stock))
                Cla_Prod=Clase_Producto.Producto(producto.id_prod,producto.nombre_prod,producto.stock,producto.precio,producto.categoria)
                Cla_Prod.mod_stock()
            messagebox.showinfo("Muchas gracias","Compra Realizada - Salir")
            #salimos a login
            self.ventana.destroy()
            FLogin.Clase_Vista_Login()
        except:
            messagebox.showerror("Error Carrito","No se pudo realizar la compra")


    def __init__(self,Cliente):
        id_cliente=Cliente.id_cliente
        self.id_cli=id_cliente
        nombre=Cliente.nombre
        apellido=Cliente.apellido
    
        self.ventana = tk.Tk()
        self.ventana.title('Venta')
        self.ventana.geometry('1200x1200')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        self.suma=0
        self.stock_carrito=0
        self.total=0
        self.Lista_Productos=[]

        # frame_form
        frame_form = tk.Frame(self.ventana, bd=0,
                              relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)

        # frame_form_top
        frame_form_top = tk.Frame(
            frame_form, height=20, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top", fill=tk.X)
        titulo = tk.Label(frame_form_top, text="Venta - Carrito", font=(
            'Times', 15), fg="#666a88", bg='#fcfcfc', pady=2)
        titulo.pack(expand=tk.YES, fill=tk.BOTH)
        # end frame_form_top

        # frame_form_fill
        frame_form_fill = tk.Frame(
            frame_form, height=20,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)
        #boton salir
        btnVolver = tk.Button(frame_form_fill, text="Salir", font=(
            'Times', 15), bg='#3a7ff6', bd=0, fg="#fff", command=self.volver_login)
        btnVolver.pack(fill=tk.X, padx=20, pady=3)
        btnVolver.bind("<Return>", (lambda event: self.volver_login()))
        
        #etiqueta Cliente
        etiqueta_usuario = tk.Label(frame_form_fill, text="usuario: "+nombre+" "+apellido , font=(
            'Times', 14), fg="#666a88", bg='#fcfcfc', anchor="center")
        etiqueta_usuario.pack(fill=tk.X, padx=20, pady=2)
        
        #boton cargar Listado de Productos
        btnCargar = tk.Button(frame_form_fill, text="Mostrar Listado de Productos", font=(
            'Times', 15), bg='#3a7ff6', bd=0, fg="#fff", command=self.llenarTabla)
        btnCargar.pack(fill=tk.X, padx=20, pady=2)
        btnCargar.bind("<Return>", (lambda event: self.llenarTabla()))

    
        #tabla contenedora de datos de todos los productos
        self.tabla=ttk.Treeview(frame_form_fill,columns=("col1","col2","col3","col4"))
        self.tabla.column("#0",width=80)
        self.tabla.column("#1",anchor="center")
        self.tabla.column("#2",anchor="center")
        self.tabla.column("#3",anchor="center")
        self.tabla.column("#4",anchor="center")

        self.tabla.heading("#0",text="ID Producto",anchor="center")
        self.tabla.heading("#1",text="Nombre",anchor="center")
        self.tabla.heading("#2",text="Cantidad",anchor="center")
        self.tabla.heading("#3",text="Precio",anchor="center")
        self.tabla.heading("#4",text="Categoria",anchor="center")
        self.tabla.pack()
        
        #etiqueta subtitulo
        etiqueta = tk.Label(frame_form_fill, text="Elija sus productos ingresando los siguientes datos (max. 30 articulos)", font=(
            'Times', 14), fg="#666a88", bg='#fcfcfc', anchor="center")
        etiqueta.pack(fill=tk.X, padx=20, pady=5)

        #etiqueta id del producto
        etiqueta_idProd = tk.Label(frame_form_fill, text="Ingrese ID del producto", font=(
            'Times', 14), fg="#666a88", bg='#fcfcfc', anchor="center")
        etiqueta_idProd.pack(fill=tk.X, padx=20, pady=5)

        #self_id_prod - entry
        self.id_prod = ttk.Entry(frame_form_fill, font=('Times', 14),state="disabled")
        self.id_prod.pack(fill=tk.Y, padx=20, pady=10,anchor="center")

        #etiqueta cantidad
        etiqueta_idProd = tk.Label(frame_form_fill, text="Ingrese cantidad deseada", font=(
            'Times', 14), fg="#666a88", bg='#fcfcfc', anchor="center")
        etiqueta_idProd.pack(fill=tk.X, padx=20, pady=5)

        #self_cantidad - entry
        self.cantidad = ttk.Entry(frame_form_fill, font=('Times', 14),state="disabled")
        self.cantidad.pack(fill=tk.Y, padx=20, pady=10,anchor="center")
        
        #boton cargar compra
        self.btnCargarCompra = tk.Button(frame_form_fill, text="Cargar al Carrito", font=(
            'Times', 15), bg='#3a7ff6', bd=0, fg="#fff", command=self.cargarCarrito,state="disabled")
        self.btnCargarCompra.pack(fill=tk.X, padx=20, pady=20)
        self.btnCargarCompra.bind("<Return>", (lambda event: self.cargarCarrito()))

        #tabla contenedora de productos seleccionados carrito
        self.tablaCarrito=ttk.Treeview(frame_form_fill,columns=("col1","col2","col3","col4"))

        self.tablaCarrito.column("#0",width=80)
        self.tablaCarrito.column("#1",anchor="center")
        self.tablaCarrito.column("#2",anchor="center")
        self.tablaCarrito.column("#3",anchor="center")
        self.tablaCarrito.column("#4",anchor="center")

        self.tablaCarrito.heading("#0",text="ID Producto",anchor="center")
        self.tablaCarrito.heading("#1",text="Nombre del Producto",anchor="center")
        self.tablaCarrito.heading("#2",text="Cantidad",anchor="center")
        self.tablaCarrito.heading("#3",text="Precio Unitario",anchor="center")
        self.tablaCarrito.heading("#4",text="SubTotal",anchor="center")
        self.tablaCarrito.pack()
        
        #etiqueta muestra total
        self.etiquetaTotal = tk.Label(frame_form_fill, text="TOTAL $"+str(self.total), font=(
            'Times', 14), fg="#666a88", bg='#fcfcfc', anchor="e")
        self.etiquetaTotal.pack(fill=tk.X, padx=200, pady=5)

        #boton Aceptar COMPRA
        self.btnComprar = tk.Button(frame_form_fill, text="AUTORIZAR / COMPRAR", font=(
            'Times', 15), bg='#3a7ff6', bd=0, fg="#fff", command=self.aceptarCompra,state="disabled")
        self.btnComprar.pack(fill=tk.X, padx=20, pady=20)
        self.btnComprar.bind("<Return>", (lambda event: self.aceptarCompra()))

        # end frame_form_fill
        self.ventana.mainloop()
#Clase_Vista_Venta()