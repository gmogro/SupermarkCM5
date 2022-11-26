
from Databases.sql import DataBase


class Cliente:
    def __init__(self,nombre,apellido,
                 ):
        self.__nombre = nombre
        
    #getters y setter
    
    def ListadoCliente(self):
        db = DataBase("supermark.db")
        cliente = db.select_all("Cliente","*")
        print(cliente)
        