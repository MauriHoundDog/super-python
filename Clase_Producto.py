from BaseDatos.Conexion_Producto import C_producto

class Producto():
    def __init__(self,id_prod,nombre_prod, stock, precio , categoria):
        self.id_prod=id_prod
        self.nombre_prod= nombre_prod
        self.stock= stock
        self.precio= precio
        self.categoria= categoria
        
    

    
    def cargar_producto(self):
        C_producto.alta_producto(self.nombre_prod,self.stock,self.precio,self.categoria)
    
    def update_producto(self):
        C_producto.modificar_idProducto(self.id_prod,self.nombre_prod,self.stock,self.precio,self.categoria)

    def mod_stock(self):
        C_producto.modificar_stock_idProducto(self.id_prod,self.stock)


