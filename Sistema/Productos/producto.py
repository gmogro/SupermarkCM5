from Databases import sql

class Producto:

    def __init__(self, codigo= "", nombre = "", precio = "", stock = "",descripcion="",id_producto = "",  id_categoria = 0):
        self.__idproducto = id_producto
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
        self.__descripcion = descripcion
        self.__idcategoria = id_categoria

    @property
    def Idproducto(self):
        return self.__idproducto
    
    @Idproducto.setter
    def Idproducto(self, id_producto):
        self.__idproducto = id_producto
    
    @property
    def Codigo(self):
        return self.__codigo
    
    @Codigo.setter
    def Codigo(self,codigo):
        self.__codigo = codigo
        
    @property
    def Nombre(self):
        return self.__nombre
    
    @Nombre.setter
    def Nombre(self, nombre):
        self.__nombre = nombre
    
    @property
    def Precio(self):
        return self.__precio
    
    @Precio.setter
    def Precio(self, precio):
        self.__precio = precio
    
    @property
    def Stock(self):
        return self.__stock
    
    @Stock.setter
    def Stock(self, stock):
        self.__stock = stock
    
    @property
    def Descripcion(self):
        return self.__descripcion
    
    @Descripcion.setter
    def Descripcion(self,descripcion):
        self.__descripcion = descripcion
        
    @property
    def Idcategoria(self):
        return self.__idcategoria
    
    @Idcategoria.setter
    def Idcategoria(self, categoria):
        self.__idcategoria = categoria
    
    def __str__(self):
        return self.__nombre + " - " + str(self.__precio) + " - " + str(self.__stock) + " - " + str(self.__idcategoria)

    def crearProducto(self):
        db = sql.DataBase('supermark.db')
        self.__codigo = input("Ingrese el codigo del Producto: ")
        self.__nombre = input("Ingrese el nombre del producto: ")
        self.__precio = float(input("Ingrese el precio del producto: "))
        self.__stock = int(input("Ingrese el stock del producto: "))
        self.__descripcion = input("Ingrese la descripcion : ")
        categorias = db.select("categoria","id_categoria,nombre","estado = 1")
        print("Nro\tNombre")
        for categoria in categorias:
            print(f"{categoria[0]}\t{categoria[1]}")
        self.__idcategoria = input("Ingrese la categoria del producto: ")
        db.insert("producto","id_categoria,codigo,nombre,precio_venta,stock,descripcion",
                  f"{self.__idcategoria},'{self.__codigo}','{self.__nombre}','{self.__precio}','{self.__stock}','{self.__descripcion}'")
        db.close()        

    def actualizarProducto(self,id_producto):
        db = sql.DataBase("supermark.db")
        print("Si no desea Modificar el Dato Solo Presione Enter")
        print("Hasta llegar al Dato que quiere modificar")
        producto = db.select("producto","id_categoria,codigo,nombre,precio_venta,stock,descripcion",f"id_producto = {id_producto} ")
        self.__codigo = input(f"Modifique el Codigo : {producto[0][1]} ")  or producto[0][1]
        self.__nombre = input(f"Modifique el Nombre :  {producto[0][1]} ") or producto[0][2]
        self.__precio = input(f"Modifique el Precio : {producto[0][3]} ")  or producto[0][3]
        self.__stock =  input(f"Modifique el Stock : {producto[0][4]} ") or producto[0][4]
        self.__descripcion = input(f"Modifique el descripcion : {producto[0][5]} ") or producto[0][5]
        categorias = db.select("categoria","id_categoria,nombre","estado = 1")
        print("Nro\tCategoria")
        for categoria in categorias:
            if producto[0][0] == categoria[0] :
                nombre = categoria[1]
            print(f"{categoria[0]} - {categoria[1]}")
        self.__idcategoria = input(f"Modifique la Categoria {nombre} Ingrese un numero : ") or producto[0][0]
        db.update("producto","codigo",f"'{self.__codigo}'",f"id_producto = {id_producto}")
        db.update("producto","nombre",f"'{self.__nombre}'",f"id_producto = {id_producto}")
        db.update("producto","precio_venta",f"'{float(self.__precio)}'",f"id_producto = {id_producto}")
        db.update("producto","stock",f"'{int(self.__stock)}'",f"id_producto = {id_producto}")
        db.update("producto","descripcion",f"'{self.__descripcion}'",f"id_producto = {id_producto}")
        db.update("producto","id_categoria",f"'{self.__idcategoria}'",f"id_producto = {id_producto}")
        db.close()
    
    def eliminarProducto(self,id_producto):
        db = sql.DataBase("supermark.db")
        db.update("producto","estado","0",f"id_producto = {id_producto}")
        db.close()
        
    def listarProducto(self):
        db = sql.DataBase("supermark.db")
        productos = db.select_all("producto","id_producto,id_categoria,codigo,nombre,precio_venta,stock,descripcion")
        print("Nro\tCategoria\tcodigo\t\tnombre\t\tprecio\tstock\tdescripcion")
        for producto in productos:
            categoria = db.select("categoria","nombre",f"id_categoria = {producto[1]}")
            print(f"{producto[0]}\t{categoria[0][0]}\t\t{producto[2]}\t\t{producto[3]}\t{producto[4]}\t{producto[5]}\t{producto[6]}")
        db.close()
    
    def select_producto(self,id_categoria = 0):
        db = sql.DataBase("supermark.db")
        productos = db.select("producto","id_producto,codigo,nombre,precio_venta,stock,descripcion",f"id_categoria = {id_categoria}")
        db.close()
        return productos