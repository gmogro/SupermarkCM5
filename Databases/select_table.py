import sql

db = sql.DataBase("supermark.db")

roles = db.select("rol","id_rol,nombre","estado = 1")
print("Nro   Role")
for rol in roles:
    print(f"{rol[0]} - {rol[1]}")

usuario = db.select("usuario","idrol,nombre,apellido,dni,email,password",
                            f"id_usuario = {1}")
usuario = input(f"Modifique el nombre {usuario[0][1]}")
print(usuario[0][1])


