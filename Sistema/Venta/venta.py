from Databases import sql
from Sistema.Productos.producto import Producto
from Sistema.Venta.cliente import Cliente
from Sistema.Venta.detalle_venta import DetalleVenta
from datetime import datetime

class Venta:

    def __init__(self, cliente = 0, tipo_comprobante="", nro_comprobante="", fecha="", total=0.0, detalle=[],id_venta = 0):
        self.__cliente = cliente
        self.__fecha = fecha
        self.__total = total
        self.__detalle = detalle
        self.__tipoComprobante = tipo_comprobante
        self.__nro_comprobante = nro_comprobante
        self.__idventa = id_venta
    
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
    def NroComprobante(self):
        return self.__nro_comprobante
    
    @NroComprobante.setter
    def NroComprobante(self,nro_comprobante):
        self.__nro_comprobante = nro_comprobante
        
    def __str__(self):
        return self.__cliente + " - " + self.__fecha + " - " + str(self.__total)
    
    def crearVenta(self):
        db = sql.DataBase("supermark.db")
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
        self.__nro_comprobante = input("Ingrese Serie de Comprobante : ")
        print("")
        print("#############Seleccione el Producto################")
        producto = Producto()
        runnig = True
        while runnig:
            producto.listarProducto()
            print("")
            id_producto = int(input("Ingrese el Nro del producto: "))
            cantidad = int(input("Ingrese la cantidad del producto: "))
            producto = db.select("producto","precio_venta",f"id_producto = {id_producto}")
            subtotal = producto[0][0] * cantidad
            detalles = DetalleVenta(id_producto, cantidad,subtotal)
            self.__total += subtotal 
            opcion = input("Desea Ingresar mas Productos 1 - SI  0 - NO : ")
            if opcion == 0:
                runnig = False
        print("####################################################")
        self.__fecha = datetime.today()
        db.insert("venta","id_cliente,tipo_comprobante,nro_comprobante,fecha,total",
                  f"'{self.__cliente}','{self.__tipoComprobante}','{self.__nro_comprobante}'"+
                  f"'{self.__fecha}','{self.__total}'")
        self.__idventa = db.get_last_id()
        for detalle in detalles:
            db.insert("detalle_venta","id_venta,id_producto,cantidad,subtotal,descuento",
                  f"'{self.__idventa}','{detalle[0]}','{detalle[1]}','{detalle[2]}'")
        db.close()
        
    def anularVenta(self,id_venta):
        db = sql.DataBase("supermark.db")
        db.update("venta","estado","ANULADA",f"WHERE id_venta = {id_venta}")
        db.close()
    
    def all_venta(self):
        db = sql.DataBase("supermark.db")
        ventas = db.select_all("venta","id_venta,id_cliente,tipo_comprobante,nro_comprobante,fecha,total,estado")
        print("#########################################################################")
        print("Nro\tCliente\t\tTipo Comprobante\tSerie Comprobante\tFecha\tTotal\tEstado")
        for venta in ventas:
            cliente = db.select("cliente","apellido|| ' ' ||nombre",f"WHERE id_cliente = {venta[1]}")
            print(f"{venta[0]}\t{cliente}\t\t{venta[2]}\t{venta[3]}\t{venta[4]}\t{venta[5]}\t{venta[6]}")
        print("#########################################################################")
        db.close()