from Databases import sql
from Productos.producto import Producto
from Venta.cliente import Cliente
from Venta.detalle_venta import DetalleVenta
from datetime import datetime

class Venta:

    def __init__(self, cliente = 0, tipo_comprobante="", serie_comprobante="", fecha="", total=0.0, detalle=[]):
        self.__cliente = cliente
        self.__fecha = fecha
        self.__total = total
        self.__detalle = detalle
        self.__tipoComprobante = tipo_comprobante
        self.__serieComprobante = serie_comprobante
    
    @property
    def Cliente(self):
        return self.__cliente
    
    @Cliente.setter
    def Cliente(self, cliente):
        self.__cliente = cliente
    
    @property
    def Fecha(self):
        return self.__fecha
    
    @Fecha.setter
    def Fecha(self, fecha):
        self.__fecha = fecha
    
    @property
    def Total(self):
        return self.__total
    
    @Total.setter
    def Total(self, total):
        self.__total = total
    
    @property
    def Detalle(self):
        return self.__detalle
    
    @Detalle.setter
    def Detalle(self, detalle):
        self.__detalle = detalle
    
    @property
    def TipoComprobante(self):
        return self.__tipoComprobante
    
    @TipoComprobante.setter
    def TipoComprobante(self,tipo_comprobante):
        self.__tipoComprobante = tipo_comprobante
        
    @property
    def SerieComprobante(self):
        return self.__serieComprobante
    
    @SerieComprobante.setter
    def SerieComprobante(self,serie_comprobante):
        self.__serieComprobante = serie_comprobante
        
    def __str__(self):
        return self.__cliente + " - " + self.__fecha + " - " + str(self.__total)
    
    def crearVenta(self):
        persona = Cliente()
        print("###################################################")
        print("Selecione un Cliente : ")
        print("Si no encuentra al Cliente dar de Alta en cliente")
        persona.listarClientes()
        print("")
        self.__cliente = input("Ingrese el Nro de Cliente : ")
        print("###################################################")
        print("")
        self.__tipoComprobante = input("Ingrese el Tipo de Comprobante : ")
        print("")
        self.__serieComprobante = input("Ingrese Serie de Comprobante : ")
        print("")
        print("#############Seleccione el Producto################")
        producto = Producto()
        runnig = True
        while runnig:
            producto.listarProducto()
            print("")
            id_producto = int(input("Ingrese el Nro del producto: "))
            cantidad = int(input("Ingrese la cantidad del producto: "))
            subtotal = producto[id_producto].Precio * cantidad
            detalle = DetalleVenta(id_producto, cantidad,subtotal)
            self.__total += subtotal 
            opcion = input("Desea Ingresar mas Productos 1 - SI  0 - NO")
            if opcion == 0:
                runnig = False
        print("####################################################")
        self.__fecha = datetime.today()
        db = sql.DataBase("supermark.db")
        db.insert("venta","id_cliente,")