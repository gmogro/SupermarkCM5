from Sistema.Login.rol import Rol
from Sistema.Login.usuario import Usuario

rol = Rol(1, "Administrador", "Administrador del sistema")

rol.create_rol()
bandera = True
while bandera:
    email = input("Email : ")
    password = input("Contraseña : ")
    usuario = Usuario()
    if (usuario.login(email,password)):
        bandera = False
    
runing = True
while runing:
    print("MENU")
    
