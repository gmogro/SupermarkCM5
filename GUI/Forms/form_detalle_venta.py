from datetime import datetime
import tkinter as tk
from tkinter import RIGHT, Y, Scrollbar, Toplevel,ttk

from Sistema.Venta.venta import Venta

class FormDetalleVenta(tk.Tk):
    
    def __init__(self,id_venta):
        super().__init__()
        self.title("Ver Venta")
        self.geometry("1060x600")
        self.iconbitmap('GUI/image/icons/tienda.ico')
        self.resizable(0,0)
        self.id_tree_detalle = 0
        self.total = 0
        self._create_form(id_venta)

    def _create_form(self,id_venta):

        venta = Venta()
        ventas = venta.get_venta(id_venta)

        form_etiqueta = ttk.Label(self, text='Ver Venta', font=("Arial bold", 25))
        form_etiqueta.grid(row=0, column=0, columnspan=2,padx=10, pady=10)

        if ventas[7] == "EXITOSA":
            form_estado = ttk.Label(self, text='Exitosa', font=("Arial bold", 25))
            form_estado.grid(row=0, column=3, columnspan=2,padx=10, pady=10)
            form_estado.config(foreground="green")
        else:
            form_estado = ttk.Label(self, text='ANULADA', font=("Arial bold", 25))
            form_estado.grid(row=0, column=3, columnspan=2,padx=10, pady=10)
            form_estado.config(foreground="red") 

        # Cliente
        cliente_etiqueta = ttk.Label(self, text='Cliente:')
        cliente_etiqueta.grid(row=1, column=0,padx=5, pady=10)
        self.cliente_entrada = ttk.Entry(self,width=50)
        self.cliente_entrada.grid(row=1,column=1,padx=5, pady=10)
        nombre_completo = ventas[1] + ", " + ventas[2]
        self.cliente_entrada.insert(0,nombre_completo)
        self.cliente_entrada.config(state="readonly")

        # Fecha
        fecha_etiqueta = ttk.Label(self, text='Fecha:')
        fecha_etiqueta.grid(row=1, column=2, sticky='W',padx=5, pady=10)
        self.fecha_entrada = ttk.Entry(self,width=50)
        self.fecha_entrada.grid(row=1, column=3, sticky='EW',padx=5, pady=10)
        fecha = datetime.strptime(ventas[5], '%Y-%m-%d %H:%M:%S.%f')
        fecha = fecha.strftime("%m/%d/%Y %H:%M:%S")
        self.fecha_entrada.insert(0,fecha)
        self.fecha_entrada.config(state="readonly")

        # Tipo Comprobante
        comprobante_etiqueta = ttk.Label(self, text='Tipo de Comprobante:')
        comprobante_etiqueta.grid(row=2, column=0,padx=5, pady=10)
        self.comprobante_entrada = ttk.Entry(self,width=50)
        self.comprobante_entrada.grid(row=2, column=1, padx=5, pady=10)
        self.comprobante_entrada.insert(0,ventas[3])
        self.comprobante_entrada.config(state="readonly")
        
        # Numero de Comprobante
        nro_comprobante_etiqueta = ttk.Label(self, text='Numero de Comprobante :')
        nro_comprobante_etiqueta.grid(row=2, column=2,sticky='W', padx=5, pady=10)
        self.nro_comprobante_entrada = ttk.Entry(self,width=50)
        self.nro_comprobante_entrada.grid(row=2, column=3,sticky='EW', padx=5, pady=10)
        self.nro_comprobante_entrada.insert(0,ventas[4])
        self.nro_comprobante_entrada.config(state="readonly")

        form_etiqueta = ttk.Label(self, text='Productos Vendidos', font=("Arial bold", 25))
        form_etiqueta.grid(row=3, column=0, columnspan=4,padx=10, pady=10)

        self.tree_detalle = ttk.Treeview(self, column=("c1", "c2", "c3","c4","c5","c5"), show='headings')
        self.tree_detalle.column("#1", anchor=tk.CENTER,width=2)
        self.tree_detalle.heading("#1", text="")
        self.tree_detalle.column("#2", anchor=tk.CENTER)
        self.tree_detalle.heading("#2", text="Producto")
        self.tree_detalle.column("#3", anchor=tk.CENTER)
        self.tree_detalle.heading("#3", text="Cantidad")
        self.tree_detalle.column("#4", anchor=tk.CENTER)
        self.tree_detalle.heading("#4", text="Precio")
        self.tree_detalle.column("#5", anchor=tk.CENTER)
        self.tree_detalle.heading("#5", text="Descuento")
        self.tree_detalle.column("#6", anchor=tk.CENTER)
        self.tree_detalle.heading("#6", text="Subtotal")
        detalles = venta.get_detalles(id_venta)
        for dt in detalles:
            dt = list(dt)
            dt[len(dt)-1] = dt[2] * dt[3]
            dt = tuple(dt)
            self.tree_detalle.insert("", tk.END, values=dt)
        self.tree_detalle.grid(row = 4, column = 0, sticky="SWE",columnspan=4,padx = 10, pady = 10)
        
        # cantidad de producto
        total_etiqueta = ttk.Label(self, text='Total :', font=("Arial", 15))
        total_etiqueta.place(x= 700 , y=460)
        self.total_entrada = ttk.Entry(self)
        self.total_entrada.grid(row = 5, column=3, sticky='E',padx=10, pady=10)
        self.total_entrada.insert(0,ventas[6])
        self.total_entrada.state(["readonly"])

        #Cancelar
        ttk.Style().configure("TButton", padding=6, relief="flat",background="#ccc")
        cancelar_boton = ttk.Button(self, text='Cerrar',command=self.cancelar)
        cancelar_boton.grid(row=6, column=3,sticky='E', padx=10, pady=20)        

    def cancelar(self):
        self.destroy()

