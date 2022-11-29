import sys
print(sys.path)
from Sistema.Login.rol import Rol
from Sistema.Login.usuario import Usuario
from Sistema.Productos.producto import Producto
from Sistema.Productos.categoria import Categoria
from os import system
from progress.bar import Bar
import time,random

""" login = True
system("cls")
while login:
    try:
        print("#####################################")
        print("##########    Login     #############")
        email = input("Email : ")
        password = input("Contraseña : ")
        usuario = Usuario()
        if (usuario.login(email,password)):
             login = False
        print("#####################################")
    except Exception as e :
        print(e + "Inicio de Session Incorrecto")
print("Has iniciado session XD")

bar = Bar('Cargando Sistema', max=100)
for num in range(100):
    time.sleep(random.uniform(0, 0.5))
    bar.next()
bar.finish()

system("cls") """
runing = True
while runing:
    print("########################################")
    print("#############  MENU  ###################")
    print("########################################")
    print("1 - Productos ")
    print("2 - Usuarios ")
    print("3 - Ventas ")
    print("0 - Salir del Sistema ")
    print("")
    opcion = int(input("Ingresa un Opcion : "))
    if opcion == 1:
        sub_opcion = -1
        while sub_opcion != 0:
            system("cls")
            print("########################################")
            print("#############  PRODUCTOS  ###################")
            print("########################################")
            print("1 - Crear Producto ")
            print("2 - Actualizar Producto ")
            print("3 - Eliminar Producto ")
            print("4 - Ver Todos los productos ")
            print("5 - Crear Categoria ")
            print("6 - Actualizar Categoria ")
            print("7 - Eliminar Categoria ")
            print("8 - Ver Todas las Categorias ")
            print("0 - Volver ")
            print("")
            sub_opcion = int(input("Ingrese un opcion : "))
            print("")
            system("cls")
            if sub_opcion == 1:
                producto = Producto()
                producto.crearProducto()
            elif sub_opcion == 2:
                producto = Producto()
                producto.listarProducto()
                print("0 - Volver ")
                print("")
                id_producto = int(input("Ingrese un numero de producto: "))
                if id_producto != 0:
                    producto.actualizarProducto(id_producto)
            elif sub_opcion == 3:
                producto = Producto()
                producto.listarProducto()
                print("0 - Volver ")
                print("")
                id_producto = int(input("Ingrese un numero de producto: "))
                if id_producto != 0:
                    producto.eliminarProducto(id_producto)
            elif sub_opcion == 4:
                producto = Producto()
                producto.listarProducto()
                volver = int(input("0 - Volver "))
            elif sub_opcion == 5:
                categoria = Categoria()
                categoria.create_categoria()
            elif sub_opcion == 6:
                categoria = Categoria()
                categoria.listar_categoria()
                print("0 - Volver ")
                id_categoria = int(input("Ingrese un numero de Categoria: "))
                if id_categoria != 0:
                    categoria.update_categoria(id_categoria)
            elif sub_opcion == 7:
                categoria = Categoria()
                categoria.listar_categoria()
                id_categoria = int(input("Ingrese un numero de Categoria: "))
                if id_categoria != 0:
                    categoria.eliminar_categoria(id_categoria)
            elif sub_opcion == 8:
                categoria = Categoria()
                categoria.listar_categoria()
                volver = int(input("0 - Volver "))
            else:
                sub_opcion = 0
    elif opcion == 2:
        sub_opcion = -1
        while sub_opcion != 0:
            system("cls")
            print("########################################")
            print("#############  Usuarios  ###############")
            print("########################################")
            print("1 - Crear Rol ")
            print("2 - Actualizar Rol ")
            print("3 - Eliminar Rol ")
            print("4 - Ver Todos los Rols ")
            print("5 - Crear Usuario ")
            print("6 - Actualizar Usuario ")
            print("7 - Eliminar Usuario ")
            print("8 - Ver Todas los Usuario ")
            print("0 - Volver ")
            print("")
            sub_opcion = int(input("Ingrese un opcion : "))
            print("")
            system("cls")
            if sub_opcion == 1:
                rol = Rol()
                rol.create_rol()
            elif sub_opcion == 2:
                rol = Rol()
                rol.all_usuario()
                print("0 - Volver ")
                print("")
                id_rol = int(input("Ingrese un numero de Rol: "))
                if id_rol != 0:
                    rol.update_rol(id_rol)
            elif sub_opcion == 3:
                rol = Rol()
                rol.all_usuario()
                print("0 - Volver ")
                print("")
                id_rol = int(input("Ingrese un numero de Rol: "))
                if id_rol != 0:
                    rol.eliminar_rol(id_rol)
            elif sub_opcion == 4:
                rol = Rol()
                rol.all_usuario()
                volver = int(input("0 - Volver "))
            elif sub_opcion == 5:
                usuario = Usuario()
                usuario.crearUsuario()
            elif sub_opcion == 6:
                usuario = Usuario()
                usuario.all_usuario()
                print("0 - Volver ")
                id_usuario = int(input("Ingrese un numero de Usuario: "))
                if id_usuario != 0:
                    usuario.modificarUsuario(id_usuario)
            elif sub_opcion == 7:
                usuario = Usuario()
                usuario.all_usuario()
                id_usuario = int(input("Ingrese un numero de Usuario: "))
                if id_usuario != 0:
                    usuario.eliminarUsuario(id_usuario)
            elif sub_opcion == 8:
                usuario = Usuario()
                usuario.all_usuario()
                volver = int(input("0 - Volver "))
            else:
                sub_opcion = 0
    elif opcion == 3:
        pass
    else:            
        runing = False
    
