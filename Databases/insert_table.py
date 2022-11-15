import sql

db = sql.DataBase("supermark.db")

db.insert("rol","nombre,descripcion","'Administrador','Administrador del sistema'")
db.insert("rol","nombre,descripcion","'Vendedor','Vendedor del sistema'")

db.insert("usuario","nombre,apellido,dni,email,password,idrol","'Mogro','Guillermo','12345678','gmogro@gmail.com','123456',1")

db.insert("persona","nombre,dni,direccion,telefono,email,tipo_persona",
          "'Mogro Guillermo Cristian','12345678','Av. Siempre Viva 123','987654321','guillermo@test.com','Cliente'")

db.close()
