from Databases import sql

class Categoria:

    def __init__(self, nombre= "", descripcion= "",id_categoria=0):
        self.__idcategoria = id_categoria
        self.__nombre = nombre
        self.__descripcion = descripcion
    
    @property
    def Idcategoria(self):
        return self.__idcategoria
    
    @Idcategoria.setter
    def Idcategoria(self,id_categoria):
        self.__idcategoria = id_categoria
        
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
        return self.__nombre + " - " + self.__descripcion

    def create_categoria(self):
        nombre = input("Nombre de la categoria : ")
        descripcion = input("Descripcion: ")
        db = sql.DataBase('supermark.db')
        db.insert("categoria","nombre,descripcion",f"'{nombre}','{descripcion}'")
        db.close()

    def update_categoria(self,id_categoria):
        db = sql.DataBase("supermark.db")
        print("Si no desea Modificar el Dato Solo Presione Enter")
        print("Hasta llegar al Dato que quiere modificar")
        categoria = db.select("categoria","id_categoria,nombre,descripcion",f"id_categoria = {id_categoria}")
        self.__nombre = input(f"Modifique el Nombre :  {categoria[0][1]} ") or categoria[0][1]
        self.__descripcion = input(f"Modifique la Descripcion : {categoria[0][2]} ") or categoria[0][2]
        db.update("categoria","nombre",f"'{self.__nombre}'",f"id_categoria = {id_categoria}")
        db.update("categoria","descripcion",f"'{self.__descripcion}'",f"id_categoria = {id_categoria}")
        db.close()

    def eliminar_categoria(self,id_categoria):
        db = sql.DataBase("supermark.db")
        db.update("categoria","estado","0",f"id_categoria = {id_categoria}")
        db.close()

    def listar_categoria(self):
        db = sql.DataBase("supermark.db")
        categorias = db.select_all("categoria","id_categoria,nombre,descripcion")
        """ print("NRO     Nombre    Descripcion")
        for categoria in categorias:
            print(f"{categoria[0]} - {categoria[1]}  -  {categoria[2]}") """
        db.close() 
        return categorias
    
    