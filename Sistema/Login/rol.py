from Databases.sql import DataBase


class Rol:
    def __init__(self, id, nombre, descripcion):
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
        return f"Nombre: {self.nombre} Descripcion: {self.descripcion}"
    
    def create_rol(self):
        print("###############")
        print("Alta de Rol")
        print("###############")
        nombre = input("Nombre: ")
        descripcion = input("Descripcion: ")
        db = DataBase('supermark.db')
        db.insert("rol","nombre,descripcion",f"'{nombre}','{descripcion}'")
        db.close()


if __name__ == "__main__":
    rol = Rol(1, "Administrador", "Administrador del sistema")
    rol.create_rol()

    
