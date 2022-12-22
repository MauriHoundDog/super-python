from BaseDatos.Conexion_Cliente import Con_Cliente

class Cliente():
    def __init__(self,id_cliente,nombre, apellido, dni , cel, email,usuario, clave):
        self.id_cliente=id_cliente
        self.nombre= nombre
        self.apellido= apellido
        self.dni= dni
        self.cel= cel
        self.email= email
        self.usuario=usuario
        self.clave= clave
    
    def __str__(self):
        id="id del cliente: "+str(self.id_cliente)
        return id

    
    def cargar_cliente(self):
        Con_Cliente.alta_cliente(self.nombre,self.apellido,self.dni,self.cel,self.email,self.usuario,self.clave)
    
    
        






#Mauro=Cliente("mauricio","navarro","35545","123213","mauro@gmail.com","1100")
#Mauro.cargar_cliente()
