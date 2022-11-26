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
    def idproducto(self):
        return self.__idproducto
    
    @idproducto.setter
    def idproducto(self, idproducto):
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

   
        
