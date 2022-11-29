from Databases import sql


class DetalleVenta:

    def __init__(self,idproducto = 0, cantidad = 0,subtotal = 0.0,id_detalleventa = 0, idventa = 0):
        self.__idDetalleVenta = id_detalleventa
        self.__cantidad = cantidad
        self.__idproducto = idproducto
        self.__idventa = idventa
        self.__subtotal = subtotal
    
    @property
    def IdDetalleVenta(self):
        return self.__IdDetalleVenta
    
    @IdDetalleVenta.setter
    def Id(self, IdDetalleVenta):
        self.__IdDetalleVenta = IdDetalleVenta
    
    @property
    def idventa(self):
        return self.__idventa
    
    @idventa.setter
    def idventa(self, idventa):
        self.__idventa = idventa
    
    @property
    def Idproducto(self):
        return self.__idproducto
    
    @Idproducto.setter
    def Idproducto(self, idproducto):
        self.__idproducto = idproducto
    
    @property
    def Cantidad(self):
        return self.__cantidad
    
    @Cantidad.setter
    def Cantidad(self, cantidad):
        self.__cantidad = cantidad
    
    @property
    def Subtotal(self):
        return self.__subtotal
    
    @Subtotal.setter
    def Subtotal(self, subtotal):
        self.__subtotal = subtotal
    
    def __str__(self):
        return self.__cantidad + " - " + self.__producto

    def get_detalleventa(self,id_venta):
        db = sql.DataBase("supermark.db")
        venta = db.select("venta","id_venta,id_cliente,tipo_comprobante,nro_comprobante,fecha,total,id_usuario",
                    f"id_venta = {id_venta}")
        cliente = db.select("persona","apellido|| ' ' ||nombre",f"id_persona = {venta[0][1]}")
        #usuario = db.select("usuario","apellido|| ' ' ||nombre",f"id_usuario = {venta[0][6]}")
        detalles = db.select("detalle_venta","id_venta,id_producto,cantidad,descuento,precio",
                    f"id_venta = {id_venta}")
        print("")
        print("")
        print('-------------------------------------------')
        print('             SUPERMARK   ')
        print('-------------------------------------------')
        print('Tipo Comprobante : ',venta[0][2],'\tnumero_comprobante : ',venta[0][3])
        print('-------------------------------------------')
        print('Cajero: Guillermo      Fecha: ',venta[0][4])
        print('-------------------------------------------')
        print('Cliente: ',cliente[0][0])
        print('-------------------------------------------')
        print('--------------DETALLES---------------------')
        print('-------------------------------------------')
        print("Nro\tproducto\tcantidad\tdescuento\tsubtotal")
        i = 0
        for detalle in detalles:
            producto = db.select("producto","nombre",f"id_producto = {detalle[1]}")
            print(f"{i}\t{producto[0][0]}\t{detalle[2]}\t{detalle[3]}\t{detalle[4]}")
            i += 1 
        print('-------------------------------------------')
        print('Total a pagar: $', venta[0][5])
        print('-------------------------------------------')
        print("")
        print("")
        db.close()
       
       

