import sql

db = sql.DataBase("supermark.db")

db.create_table("rol","id_rol INTEGER PRIMARY KEY AUTOINCREMENT," +  
                       "nombre TEXT," + 
                       "descripcion TEXT," + 
                       "estado INTEGER DEFAULT 1"
                )

db.create_table("usuario","id_usuario INTEGER PRIMARY KEY AUTOINCREMENT," +
                          "nombre TEXT," +
                          "apellido TEXT," +
                          "dni TEXT," +
                          "email TEXT,"  +
                          "password TEXT," + 
                          "idrol INTEGER," +
                          "estado INTEGER DEFAULT 1" 
                )

db.create_table("persona","id_persona INTEGER PRIMARY KEY AUTOINCREMENT," +
                        "nombre TEXT(50)," +
                        "apellido TEXT(50)," +
                        "dni TEXT(11)," + 
                        "direccion TEXT(50)," +
                        "fecha_nacimiento TEXT(20)," +
                        "telefono TEXT(9)," +
                        "email TEXT(50)," +
                        "tipo_persona TEXT(20) DEFAULT 'Cliente'," +
                        "tipo_responsabilidad TEXT(30),"+
                        "estado INTEGER DEFAULT 1"
                )

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

db.create_table("detalle_venta", 
                "id_detalle_venta INTEGER PRIMARY KEY AUTOINCREMENT,"+
                "id_venta INTEGER,"+
                "id_producto INTEGER,"+
                "cantidad INTEGER,"+
                "precio REAL,"+
                "descuento REAL DEFAULT 0"
                )

db.create_table("producto",
                "id_producto INTEGER PRIMARY KEY AUTOINCREMENT,"+
                "id_categoria INTEGER,"+
                "codigo TEXT(20)," +
                "nombre TEXT(50),"+
                "precio_venta REAL,"+
                "stock INTEGER,"+
                "descripcion TEXT(256),"+
                "estado INTEGER DEFAULT 1"
                )

db.create_table("categoria",
                "id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,"+
                "nombre TEXT(50),"+
                "descripcion TEXT(256),"+
                "estado INTEGER DEFAULT 1"
                )

db.close()
