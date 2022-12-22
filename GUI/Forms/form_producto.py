import tkinter as tk
from tkinter import ttk,Toplevel,Label
from tkinter import messagebox
from tkcalendar import DateEntry
from GUI import principal
from Sistema.Productos.categoria import Categoria

from Sistema.Venta.cliente import Cliente

class FormProducto(Toplevel):
    def __init__(self,master):
        super().__init__()
        self.master = master
        self.title("Crear Producto")
        self.geometry("680x500")
        self.iconbitmap('GUI/image/icons/tienda.ico')
        self.resizable(0,0)
        self.columnconfigure(1, weight=2)
        self._create_label_input()

    def _create_label_input(self):

        form_etiqueta = ttk.Label(self, text='Crear Producto', font=("Arial", 25))
        form_etiqueta.grid(row=0, column=0, columnspan=2,padx=20, pady=20)

        #Categoria
        categoria_etiqueta = ttk.Label(self, text='Categoria :')
        categoria_etiqueta.grid(row=1, column=0, sticky='W', padx=5, pady=5)
        categoria = Categoria()
        categorias = categoria.listar_categoria()
        val_categoria = []
        for cat in categorias :
            categoria_value = "_".join(str(v) for v in cat)
            val_categoria.append(categoria_value)
        self.categoria_entrada = ttk.Combobox(self,values=val_categoria)
        self.categoria_entrada.grid(row=1, column=1, sticky='EW', padx=5, pady=5)

        # codigo
        codigo_etiqueta = ttk.Label(self, text='Codigo:')
        codigo_etiqueta.grid(row=2, column=0, sticky='W',padx=5, pady=10)
        self.codigo_entrada = ttk.Entry(self)
        self.codigo_entrada.grid(row=2, column=1, sticky='EW',padx=5, pady=10)

        # nombre producto
        nombre_etiqueta = ttk.Label(self, text='Nombre:')
        nombre_etiqueta.grid(row=3, column=0, sticky='W', padx=5, pady=10)
        self.nombre_entrada = ttk.Entry(self)
        self.nombre_entrada.grid(row=3, column=1, sticky='EW', padx=5, pady=10)

        # stock
        stock_etiqueta = ttk.Label(self, text='Stock:')
        stock_etiqueta.grid(row=4, column=0, sticky='W',padx=5, pady=10)
        self.stock_entrada = ttk.Entry(self)
        self.stock_entrada.grid(row=4, column=1, sticky='EW',padx=5, pady=10)

        # Precio
        precio_venta_etiqueta = ttk.Label(self, text='Direccion:')
        precio_venta_etiqueta.grid(row=5, column=0, sticky='W', padx=5, pady=10)
        self.precio_venta_entrada = ttk.Entry(self)
        self.precio_venta_entrada.grid(row=5, column=1, sticky='EW', padx=5, pady=10)

        # Descripcion
        descripcion_etiqueta = ttk.Label(self, text='Descripcion:')
        descripcion_etiqueta.grid(row=6, column=0, sticky='W',padx=5, pady=10)
        self.descripcion_entrada = ttk.Entry(self)
        self.descripcion_entrada.grid(row=6, column=1, sticky='EW',padx=5, pady=10)

        #Aceptar
        ttk.Style().configure("TButton", padding=6, relief="flat",background="#ccc")
        aceptar_boton = ttk.Button(self, text='Aceptar',command=self.aceptar)
        aceptar_boton.grid(row=7, column=1,sticky='E', padx=100, pady=20)
        #Cancelar
        cancelar_boton = ttk.Button(self, text='Cancelar',command=self.cancelar)
        cancelar_boton.grid(row=7, column=1,sticky='E', padx=5, pady=20)

    def aceptar(self):
        pass
        ''' if self.id_cliente_entrada.get() == "":
            cliente = Cliente(self.nombre_entrada.get(),self.apellido_entrada.get(),self.direccion_entrada.get(),
                            self.telefono_entrada.get(),self.fecha_nacimiento_entrada.get(),
                            self.dni_entrada.get(),self.email_entrada.get(),self.tipo_responsabilidad_entrada.get())
            cliente.crearCliente()
            self.refresh()
        else:
            cliente = Cliente(self.nombre_entrada.get(),self.apellido_entrada.get(),self.direccion_entrada.get(),
                            self.telefono_entrada.get(),self.fecha_nacimiento_entrada.get(),
                            self.dni_entrada.get(),self.email_entrada.get(),self.tipo_responsabilidad_entrada.get(),
                            self.id_cliente_entrada.get())
            cliente.modificarCliente()
            self.refresh()
        self.destroy() '''
    
    def cancelar(self):
        self.destroy()
    
    def refresh(self):
        self.destroy()
        self.master.destroy()
        self.master = principal.Main()
        self.master.btnInfo.invoke()
        self.master.mainloop()
   
        
