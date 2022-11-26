
class Persona:

    def __init__(self, nombre, apellido, direccion, telefono,fecha_nacimiento, dni):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__direccion = direccion
        self.__telefono = telefono
        self.__fecha_nacimiento = fecha_nacimiento
        self.__dni = dni

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
    def Direccion(self):
        return self.__direccion
    
    @Direccion.setter
    def Direccion(self, direccion):
        self.__direccion = direccion
    
    @property
    def Telefono(self):
        return self.__telefono
    
    @Telefono.setter
    def Telefono(self, telefono):
        self.__telefono = telefono
    
    @property
    def Fecha_nacimiento(self):
        return self.__fecha_nacimiento
    
    @Fecha_nacimiento.setter
    def Fecha_nacimiento(self, fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento
    
    @property
    def Dni(self):
        return self.__dni
    
    @Dni.setter
    def Dni(self, dni):
        self.__dni = dni
    
    def __str__(self):
        return self.__nombre + " " + self.__apellido + " - " + self.__direccion + " - " + self.__telefono