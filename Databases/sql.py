#EN ESTA clase TRABAJAREMOS TODO LO QUE es CONSULTAs CON LA BASES DE DATOS
import sqlite3
class  DataBase:
    def __init__(self, name):
        self.name = name
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()
    
    def create_table(self, table_name, columns):
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns});")
        self.connection.commit()
    
    def insert(self, table_name, columns, values):
        self.cursor.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({values});")
        self.connection.commit()
    
    def select(self, table_name, columns, condition):
        self.cursor.execute(f"SELECT {columns} FROM {table_name} WHERE {condition}")
        return self.cursor.fetchall()
    
    def select_all(self, table_name, columns):
        self.cursor.execute(f"SELECT {columns} FROM {table_name}")
        return self.cursor.fetchall()
    
    def update(self, table_name, column, value, condition):
        self.cursor.execute(f"UPDATE {table_name} SET {column} = {value} WHERE {condition}")
        self.connection.commit()
    
    def delete(self, table_name, condition):
        self.cursor.execute(f"DELETE FROM {table_name} WHERE {condition}")
        self.connection.commit()
    
    def delete_table(self, table_name):
        self.cursor.execute(f"DROP TABLE {table_name}")
        self.connection.commit()
    
    def close(self):
        self.connection.close()
    
    def __str__(self):
        return f"DataBase({self.name})"
