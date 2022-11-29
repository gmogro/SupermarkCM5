import sqlite3
import sql

connection = sqlite3.connect('supermark.db')
connection.execute("DROP TABLE venta")
print("data dropped successfully")
connection.close()


db = sql.DataBase("supermark.db")
db.create_table("venta",
                "id_venta INTEGER PRIMARY KEY AUTOINCREMENT,"+
                "id_cliente INTEGER,"+
                "tipo_comprobante TEXT(20),"+
                "nro_comprobante TEXT(7),"+
                "fecha datetime,"+
                "total REAL,"+
                "estado TEXT(20) DEFAULT 'EXITOSA',"+
                "id_usuario INTEGER"
                )

db.close()