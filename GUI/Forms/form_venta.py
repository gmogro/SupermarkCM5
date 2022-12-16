from datetime import datetime
import tkinter as tk
from tkinter import Toplevel,ttk
from Sistema.Productos.categoria import Categoria
from Sistema.Productos.producto import Producto
from Sistema.Venta.cliente import Cliente

class FormVenta(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title("Crear Venta")
        self.geometry("680x500")
        self.iconbitmap('GUI/image/icons/tienda.ico')
        self.resizable(0,0)
        self.columnconfigure(1, weight=2)
        self._create_form()

    def _create_form(self):

        form_etiqueta = ttk.Label(self, text='Crear Venta', font=("Arial", 25))
        form_etiqueta.grid(row=0, column=0, columnspan=2,padx=20, pady=20)

        # Cliente
        cliente_etiqueta = ttk.Label(self, text='Cliente:')
        cliente_etiqueta.grid(row=1, column=0, sticky='W', padx=5, pady=10)
        cliente = Cliente()
        clientes = cliente.select_cliente()
        self.cliente_entrada = ttk.Combobox(self,values=clientes)
        self.cliente_entrada.grid(row=1, column=1, sticky='EW', padx=5, pady=10)
        
        # Tipo Comprobante
        comprobante_etiqueta = ttk.Label(self, text='Tipo de Comprobante:')
        comprobante_etiqueta.grid(row=2, column=0, sticky='W', padx=5, pady=10)
        self.comprobante_entrada = ttk.Combobox(self,values=['Factura','Ticket Comun','Nota Credito'])
        self.comprobante_entrada.grid(row=2, column=1, sticky='EW', padx=5, pady=10)
        
        # Numero de Comprobante
        nro_comprobante_etiqueta = ttk.Label(self, text='Numero de Comprobante :')
        nro_comprobante_etiqueta.grid(row=3, column=0, sticky='W', padx=5, pady=10)
        self.nro_comprobante_entrada = ttk.Entry(self)
        self.nro_comprobante_entrada.grid(row=3, column=1, sticky='EW', padx=5, pady=10)

        # Fecha
        fecha_etiqueta = ttk.Label(self, text='Fecha:')
        fecha_etiqueta.grid(row=4, column=0, sticky='W',padx=5, pady=10)
        self.fecha_entrada = ttk.Entry(self)
        self.fecha_entrada.grid(row=4, column=1, sticky='EW',padx=5, pady=10)
        today = datetime.today().strftime("%d/%m/%Y")
        self.fecha_entrada.insert(0,today)

        form_etiqueta = ttk.Label(self, text='Seleccione Productos', font=("Arial", 15))
        form_etiqueta.grid(row=5, column=0, columnspan=2,padx=20, pady=10)
        
        #Categoria
        categoria_etiqueta = ttk.Label(self, text='Categoria :')
        categoria_etiqueta.grid(row=6, column=0, sticky='W', padx=5, pady=5)
        categoria = Categoria()
        categorias = categoria.listar_categoria()
        self.categoria_entrada = ttk.Combobox(self,values=categorias)
        self.categoria_entrada.grid(row=6, column=1, sticky='EW', padx=5, pady=5)
        
        # producto
        producto_etiqueta = ttk.Label(self, text='Producto :')
        producto_etiqueta.grid(row=7, column=0, sticky='W', padx=5, pady=10)
        producto = Producto()
        productos = producto.select_producto()
        self.producto_entrada = ttk.Combobox(self,values=productos)
        self.producto_entrada.grid(row=7, column=1, sticky='EW', padx=5, pady=10)

        # Stock
        cantidad_etiqueta = ttk.Label(self, text='Cantidad:')
        cantidad_etiqueta.grid(row=8, column=0, sticky='W',padx=5, pady=10)
        self.cantidad_entrada = ttk.Entry(self)
        self.cantidad_entrada.grid(row=8, column=1, sticky='EW',padx=5, pady=10)
        
        # boton agregar
        login_boton = ttk.Button(self, text='Agregar')
        login_boton.grid(row=9, column=0, columnspan=2)
        
        """ #Aceptar
        ttk.Style().configure("TButton", padding=6, relief="flat",background="#ccc")
        aceptar_boton = ttk.Button(self, text='Aceptar',command=self.aceptar)
        aceptar_boton.grid(row=9, column=1,sticky='E', padx=100, pady=20)
        #Cancelar
        cancelar_boton = ttk.Button(self, text='Cancelar',command=self.cancelar)
        cancelar_boton.grid(row=9, column=1,sticky='E', padx=5, pady=20) """

    """ def aceptar(self):
        cliente = Cliente(self.nombre_entrada.get(),self.apellido_entrada.get(),self.dni_entrada.get(),
                          self.direccion_entrada.get(),self.stock_nacimiento_entrada.get(),
                          self.telefono_entrada.get(),self.email_entrada.get(),self.producto_entrada.get())
        cliente.crearCliente()
        self.destroy()

    def cancelar(self):
        self.destroy() """

if __name__ == '__main__':
    app = FormVenta()
    app.mainloop()