from Databases import sql
class Usuario:

    def __init__(self, id=0, nombre="", apellido="", dni="", email="", password="", idrol=0, estado=1):
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__email = email
        self.__password = password
        self.__idrol = idrol
        self.__estado = estado

    @property
    def Id(self):
        return self.__id

    @Id.setter
    def Id(self, id):
        self.__id = id

    @property
    def Nombre(self):
        return self.__nombre
    
    @Nombre.setter
    def Nombre(self, nombre):
        self.__nombre = nombre
    
    @property
    def Apellido(self):
        return self.__apellido
    
    @Apellido.setter
    def Apellido(self, apellido):
        self.__apellido = apellido
    
    @property
    def Dni(self):
        return self.__dni
    
    @Dni.setter
    def Dni(self,dni):
        self.__dni = dni
        
    @property
    def Email(self):
        return self.__email
    
    @Email.setter
    def Email(self, email):
        self.__email = email
    
    @property
    def Password(self):
        return self.__password
    
    @Password.setter
    def Password(self, password):
        self.__password = password
    
    @property
    def Idrol(self):
        return self.__idrol
    
    @Idrol.setter
    def Idrol(self,idrol):
        self.__idrol = idrol
        
    @property
    def Estado(self):
        return self.__estado
    
    @Estado.setter
    def Estado(self, estado):
        self.__estado = estado
    
    def __str__(self):
        return self.__nombre + " - " + self.__apellido + " - " + " - " + self.__email + " - " + self.__password

    def crearUsuario(self):
        self.__nombre = input("Ingrese el nombre del usuario: ")
        self.__apellido = input("Ingrese el apellido del usuario: ")
        self.__dni = input("Ingrese el DNI: ")
        self.__email = input("Ingrese el email del usuario: ")
        self.__password = input("Ingrese el password del usuario: ")
        print("Elija un Rol para este Usuario")
        db = sql.DataBase("supermark.db")
        roles = db.select("rol","id_rol,nombre","estado = 1")
        print("Nro   Role")
        for rol in roles:
            print(f"{rol[0]} - {rol[1]}")
        self.__idrol = input("Ingrese el numero correspondiente al Rol : ")
        db.insert("usuario","nombre,apellido,dni,email,password,idrol",
                  f"'{self.__nombre}','{self.__apellido}','{self.__dni}','{self.__email}','{self.__password}',{self.__idrol}")
        db.close()
        

    def login(self,email,password):
        db = sql.DataBase("supermark.db")
        usuario = db.select("usuario","password",f"email = '{email}'")
        if len(usuario)>0:
            self.__password = usuario[0][0]
            db.close()
            if self.__password == password:
                return True
            else:
                print("Contraseña Incorrecta....")
                return False
        else:
            print("Usuario incorrecto ó ")
            print("No se encuentra Registrado el Usuario")
            return False
        
    def logout(self):
        self.__email = ""
        self.__password = ""
    
    def modificarUsuario(self,id_usuario):
        db = sql.DataBase("supermark.db")
        print("Si no desea Modificar el Dato Solo Presione Enter")
        print("Hasta llegar al Dato que quiere modificar")
        usuario = db.select("usuario","idrol,nombre,apellido,dni,email,password",f"id_usuario = {id_usuario} ")
        self.__nombre = input(f"Modifique el Nombre :  {usuario[0][1]} ") or usuario[0][1]
        self.__apellido = input(f"Modifique el Apellido : {usuario[0][2]} ") or usuario[0][2]
        self.__dni = input(f"Modifique el DNI : {usuario[0][3]} ") or usuario[0][3]
        self.__email = input(f"Modifique el email : {usuario[0][4]} ") or usuario[0][4]
        self.__password = input(f"Modifique el password : {usuario[0][5]} ") or usuario[0][5]
        roles = db.select("rol","id_rol,nombre","estado = 1")
        print("Nro   Role")
        for rol in roles:
            if usuario[0][0] == rol[0] :
                nombre = rol[1]
            print(f"{rol[0]} - {rol[1]}")
        self.__idrol = input(f"Modifique el Rol {nombre} Ingrese un numero : ") or usuario[0][0]
        db.update("usuario","nombre",f"'{self.__nombre}'",f"id_usuario = {id_usuario}")
        db.update("usuario","apellido",f"'{self.__apellido}'",f"id_usuario = {id_usuario}")
        db.update("usuario","dni",f"'{self.__dni}'",f"id_usuario = {id_usuario}")
        db.update("usuario","email",f"'{self.__email}'",f"id_usuario = {id_usuario}")
        db.update("usuario","password",f"'{self.__password}'",f"id_usuario = {id_usuario}")
        db.update("usuario","idrol",f"'{self.__idrol}'",f"id_usuario = {id_usuario}")
        db.close()
        
    def eliminarUsuario(self,id_usuario):
        db = sql.DataBase("supermark.db")
        db.update("usuario","estado","0",f"id_usuario = {id_usuario}")
        db.close()
    
    def all_usuario(self):
        db = sql.DataBase("supermark.db")
        usuario = db.select_all("usuario","id_usuario,nombre,apellido,dni,email,idrol")
        print("NRO\tNombre\tApellido\tdni\temail\trol")
        for user in usuario:
            rol = db.select("rol","nombre",f"id_rol = '{user[5]}'")
            print(f"{user[0]}\t{user[1]}\t{user[2]}\t{user[3]}\t{user[4]}\t{rol[0][0]}")
        db.close() 
