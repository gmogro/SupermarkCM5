from Databases import sql


class Rol:
    def __init__(self, id = 0, nombre = "", descripcion = ""):
        self.__id = id
        self.__nombre = nombre
        self.__descripcion = descripcion

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
    def Descripcion(self):
        return self.__descripcion
    
    @Descripcion.setter
    def Descripcion(self, descripcion):
        self.__descripcion = descripcion
    
    def __str__(self):
        return f"Nombre: {self.__nombre} Descripcion: {self.__descripcion}"
    
    def create_rol(self):
        nombre = input("Nombre: ")
        descripcion = input("Descripcion: ")
        db = sql.DataBase('supermark.db')
        db.insert("rol","nombre,descripcion",f"'{nombre}','{descripcion}'")
        db.close()

    def update_rol(self,id_rol):
        db = sql.DataBase("supermark.db")
        print("Si no desea Modificar el Dato Solo Presione Enter")
        print("Hasta llegar al Dato que quiere modificar")
        rol = db.select("rol","id_rol,nombre,descripcion",f"id_rol = {id_rol}")
        self.__nombre = input(f"Modifique el Nombre :  {rol[0][1]} ") or rol[0][1]
        self.__descripcion = input(f"Modifique la Descripcion : {rol[0][2]} ") or rol[0][2]
        db.update("rol","nombre",f"'{self.__nombre}'",f"id_rol = {id_rol}")
        db.update("rol","descripcion",f"'{self.__descripcion}'",f"id_rol = {id_rol}")
        db.close()

    def eliminar_rol(self,id_rol):
        db = sql.DataBase("supermark.db")
        db.update("rol","estado","0",f"id_rol = {id_rol}")
        db.close()

    def all_rol(self):
        db = sql.DataBase("supermark.db")
        roles = db.select_all("rol","id_rol,nombre,descripcion")
        print("NRO     Nombre    Descripcion")
        for rol in roles:
            print(f"{rol[0]} - {rol[1]}  -  {rol[2]}")
        db.close() 
    
