from Databases import sql
from Venta.persona import Persona


class Cliente(Persona):

    def __init__(self,id_cliente = 0, nombre = "", apellido="", direccion="", telefono="", fecha_nacimiento="", dni="", email="", tipo_responsabilidad=""):
        self.__idcliente = id_cliente
        super().__init__(nombre, apellido, direccion, telefono, fecha_nacimiento,dni)
        self.__email = email
        self.__tipo_responsabilidad = tipo_responsabilidad
        self.__estado = True

    @property
    def Idcliente(self):
        return self.__idcliente
    
    @Idcliente.setter
    def Idcliente(self, idcliente):
        self.__idcliente = idcliente
    
    @property
    def Email(self):
        return self.__email
    
    @Email.setter
    def Email(self, email):
        self.__email = email
    
    @property
    def Tipo_responsabilidad(self):
        return self.__tipo_responsabilidad
    
    @Tipo_responsabilidad.setter
    def Tipo_responsabilidad(self, tipo_responsabilidad):
        self.__tipo_responsabilidad = tipo_responsabilidad
    
    @property
    def Estado(self):
        return self.__estado
    
    @Estado.setter
    def Estado(self, estado):
        self.__estado = estado
    
    def __str__(self):
        return super().__str__() + " - " + self.__email + " - " + self.__tipo_responsabilidad + " - " + self.__estado
    
    def crearCliente(self):
        super().Nombre    = input("Ingrese el nombre del cliente: ")
        super().Apellido  = input("Ingrese el apellido del cliente: ")
        super().Direccion = input("Ingrese la direccion del cliente: ")
        super().Telefono  = input("Ingrese el telefono del cliente: ")
        super().Fecha_nacimiento = input("Ingrese la fecha de nacimiento del cliente: ")
        super().Dni = input("Ingrese el dni del cliente: ")
        self.__email = input("Ingrese el email del cliente: ")
        self.__tipo_responsabilidad = input("Ingrese el tipo de responsabilidad del cliente: ")
        db = sql.DataBase('supermark.db')
        db.insert("cliente","nombre,apellido,dni,direccion,telefono,fecha_nacimiento,email,tipo_responsabilidad",
                  f"'{super().Nombre}','{super().Apellido}','{super().Dni}',"+
                  f"{super().Direccion},'{super().Telefono}','{super().Fecha_nacimiento}',"+
                  f"'{self.__email}','{self.__tipo_responsabilidad}'"
                  )
        db.close()
        
    def modificarCliente(self,id_cliente):
        db = sql.DataBase('supermark.db')
        cliente = db.select("persona","nombre,apellido,dni,direccion,telefono,fecha_nacimiento,email,tipo_responsabilidad",
                  f"id_persona = {id_cliente}")
        print("Si no desea Modificar el Dato Solo Presione Enter")
        print("Hasta llegar al Dato que quiere modificar")
        super().Nombre    = input(f"Modifica el Nombre {cliente[0][0]} : ") or cliente[0][0]
        super().Apellido  = input(f"Modifica el Apellido {cliente[0][1]} : ") or cliente[0][1]
        super().Dni = input(f"Modifica el DNI : {cliente[0][2]}") or cliente[0][2]
        super().Direccion = input(f"Modifica la Direccion {cliente[0][3]}: ") or cliente[0][3]
        super().Telefono  = input(f"Modifica el telefono {cliente[0][4]}: ")
        super().Fecha_nacimiento = input(f"Modifica la fecha de nacimiento {cliente[0][5]} :") or cliente[0][5]
        self.__email = input(f"Modifica email {cliente[0][6]}: ") or cliente[0][6]
        self.__tipo_responsabilidad = input(f"Modifica el tipo de responsabilidad {cliente[0][7]} :") or cliente[0][7]
        db.update("persona","nombre",f"'{super().Nombre}'",f"id_persona = {id_cliente}")
        db.update("persona","apellido",f"'{super().Apellido}'",f"id_persona = {id_cliente}")
        db.update("persona","dni",f"'{super().Dni}'",f"id_persona = {id_cliente}")
        db.update("persona","direccion",f"'{super().Direccion}'",f"id_persona = {id_cliente}")
        db.update("persona","telefono",f"'{super().Telefono}'",f"id_persona = {id_cliente}")
        db.update("persona","fecha_nacimiento",f"'{super().Fecha_nacimiento}'",f"id_persona = {id_cliente}")
        db.update("persona","email",f"'{self.__email}'",f"id_persona = {id_cliente}")
        db.update("persona","tipo_responsabilidad",f"'{self.__tipo_responsabilidad }'",f"id_persona = {id_cliente}")
        db.close()
    
    def eliminarCliente(self,id_cliente):
        self.__estado = 0
        db = sql.DataBase("supermark.db")
        db.update("persona","estado",f"'{self.__estado}'",f"id_persona = {id_cliente}")
        db.close()
    
    def listarClientes(self):
        db = sql.DataBase("supermark.db")
        clientes = db.select_all("clientes","id_persona,nombre,apellido,dni,direccion,telefono,fecha_nacimiento,email,tipo_responsabilidad")
        print("Nro\tnombre\tapellido\tdni\tdireccion\t\ttelefono\tfecha_nacimiento\temail\ttipo_responsabilidad")
        for cliente in clientes:
            print(f"{cliente[0]}\t{cliente[1]}\t{cliente[2]}\t{cliente[3]}\t{cliente[4]}\t\t{cliente[5]}\t{cliente[6]}\t{cliente[7]}\t{cliente[8]}")
        db.close()       
        
