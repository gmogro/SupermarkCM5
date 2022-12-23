from datetime import datetime
import tkinter as tk
from tkinter import RIGHT, Y, Scrollbar, Toplevel,ttk
from Sistema.Productos.categoria import Categoria
from Sistema.Productos.producto import Producto
from Sistema.Venta.cliente import Cliente
from Sistema.Venta.detalle_venta import DetalleVenta
from Sistema.Venta.venta import Venta
from GUI import principal

class FormDetalleVenta(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title("Ver Venta")
        self.geometry("940x600")
        self.iconbitmap('GUI/image/icons/tienda.ico')
        self.resizable(0,0)
        self.id_tree_detalle = 0
        self.total = 0
        self._create_form()

    def _create_form(self):

        form_etiqueta = ttk.Label(self, text='Ver Venta', font=("Arial", 25))
        form_etiqueta.grid(row=0, column=0, columnspan=4,padx=10, pady=10)

        # Cliente
        cliente_etiqueta = ttk.Label(self, text='Cliente:')
        cliente_etiqueta.grid(row=1, column=0,padx=5, pady=10)
        cliente_entrada = ttk.Entry(self,width=50)
        cliente_entrada.grid(row=1,column=1,padx=5, pady=10)

        # Fecha
        fecha_etiqueta = ttk.Label(self, text='Fecha:')
        fecha_etiqueta.grid(row=1, column=2, sticky='W',padx=5, pady=10)
        self.fecha_entrada = ttk.Entry(self,width=50)
        self.fecha_entrada.grid(row=1, column=3, sticky='EW',padx=5, pady=10)
        today = datetime.today().strftime("%d/%m/%Y")
        self.fecha_entrada.insert(0,today)
        self.fecha_entrada.config(state="readonly")

        # Tipo Comprobante
        comprobante_etiqueta = ttk.Label(self, text='Tipo de Comprobante:')
        comprobante_etiqueta.grid(row=2, column=0,padx=5, pady=10)
        self.comprobante_entrada = ttk.Entry(self,width=50)
        self.comprobante_entrada.grid(row=2, column=1, padx=5, pady=10)
        
        # Numero de Comprobante
        nro_comprobante_etiqueta = ttk.Label(self, text='Numero de Comprobante :')
        nro_comprobante_etiqueta.grid(row=2, column=2,padx=5, pady=10)
        self.nro_comprobante_entrada = ttk.Entry(self,width=50)
        self.nro_comprobante_entrada.grid(row=2, column=3,padx=5, pady=10)

        form_etiqueta = ttk.Label(self, text='Producto Vendidos', font=("Arial", 25))
        form_etiqueta.grid(row=3, column=0, columnspan=4,padx=10, pady=10)

        self.tree_detalle = ttk.Treeview(self, column=("c1", "c2", "c3","c4"), show='headings')
        self.tree_detalle.column("#1", anchor=tk.CENTER)
        self.tree_detalle.heading("#1", text="Nro")
        self.tree_detalle.column("#2", anchor=tk.CENTER)
        self.tree_detalle.heading("#2", text="Producto")
        self.tree_detalle.column("#3", anchor=tk.CENTER)
        self.tree_detalle.heading("#3", text="Cantidad")
        self.tree_detalle.column("#4", anchor=tk.CENTER)
        self.tree_detalle.heading("#4", text="Subtotal")
        self.tree_detalle.grid(row = 4, column = 0, sticky="SWE",columnspan=4,padx = 10, pady = 10)
        
        # cantidad de producto
        total_etiqueta = ttk.Label(self, text='Total :', font=("Arial", 15))
        total_etiqueta.place(x= 700 , y=460)
        self.total_entrada = ttk.Entry(self)
        self.total_entrada.grid(row = 5, column=3, sticky='E',padx=10, pady=10)
        self.total_entrada.state(["readonly"])

        #Cancelar
        ttk.Style().configure("TButton", padding=6, relief="flat",background="#ccc")
        cancelar_boton = ttk.Button(self, text='Cerrar',command=self.cancelar)
        cancelar_boton.grid(row=6, column=3,sticky='E', padx=10, pady=20)        

    def cancelar(self):
        self.destroy()

