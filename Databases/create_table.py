import sql

db = sql.DataBase("supermark.db")
""" db.delete_table("Cliente")
db.delete_table("Venta")
db.close() """

db.create_table("Cliente",
                "id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"+
                "nombre TEXT(50) NOT NULL,"+
                "dni TEXT(11) NOT NULL")

db.create_table("Venta",
                "id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"+
                "id_cliente INTEGER,"
                "fecha TEXT(10) NOT NULL,"+
                "total REAL NOT NULL,"
                "FOREIGN KEY(id_cliente) REFERENCES Cliente(id)")
db.close()
