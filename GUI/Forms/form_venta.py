from datetime import datetime
import tkinter as tk
from tkinter import RIGHT, Y, Scrollbar, Toplevel,ttk
from Sistema.Productos.categoria import Categoria
from Sistema.Productos.producto import Producto
from Sistema.Venta.cliente import Cliente
from Sistema.Venta.detalle_venta import DetalleVenta
from Sistema.Venta.venta import Venta
from GUI import principal

class FormVenta(tk.Tk):
    
    def __init__(self,master):
        super().__init__()
        self.title("Crear Venta")
        self.geometry("960x760")
        self.iconbitmap('GUI/image/icons/tienda.ico')
        self.resizable(0,0)
        self.columnconfigure(1, weight=2)
        self.id_tree_detalle = 0
        self.total = 0
        self._create_form()

    def _create_form(self):

        form_etiqueta = ttk.Label(self, text='Crear Venta', font=("Arial", 25))
        form_etiqueta.grid(row=0, column=0, columnspan=2,padx=10, pady=10)

        # Cliente
        cliente_etiqueta = ttk.Label(self, text='Cliente:')
        cliente_etiqueta.grid(row=1, column=0, sticky='W', padx=5, pady=10)
        cliente = Cliente()
        clientes = cliente.select_cliente()
        val_cliente = []
        for cl in clientes :
            cliente_value = "_".join(str(v) for v in cl)
            val_cliente.append(cliente_value)
        self.cliente_entrada = ttk.Combobox(self,values=val_cliente)
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
        self.fecha_entrada.config(state="readonly")

        form_etiqueta = ttk.Label(self, text='Seleccione Productos', font=("Arial", 15))
        form_etiqueta.grid(row=5, column=0, columnspan=2,padx=5, pady=5)
        
        #Categoria
        categoria_etiqueta = ttk.Label(self, text='Categoria :')
        categoria_etiqueta.grid(row=6, column=0, sticky='W', padx=5, pady=5)
        categoria = Categoria()
        categorias = categoria.listar_categoria()
        val_categoria = []
        for cat in categorias :
            categoria_value = "_".join(str(v) for v in cat)
            val_categoria.append(categoria_value)
        self.categoria_entrada = ttk.Combobox(self,values=val_categoria)
        self.categoria_entrada.grid(row=6, column=1, sticky='EW', padx=5, pady=5)
        self.categoria_entrada.bind("<<ComboboxSelected>>", lambda event: self.add_product_combobox(event))
        
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
        login_boton = ttk.Button(self, text='Agregar', command= self.agregar)
        login_boton.grid(row=9, column=0, columnspan=2)
        
        self.tree_detalle = ttk.Treeview(self, column=("c1", "c2", "c3","c4"), show='headings')
        self.tree_detalle.column("#1", anchor=tk.CENTER, minwidth = 4)
        self.tree_detalle.heading("#1", text="Nro")
        self.tree_detalle.column("#2", anchor=tk.CENTER)
        self.tree_detalle.heading("#2", text="Producto")
        self.tree_detalle.column("#3", anchor=tk.CENTER)
        self.tree_detalle.heading("#3", text="Cantidad")
        self.tree_detalle.column("#4", anchor=tk.CENTER)
        self.tree_detalle.heading("#4", text="Subtotal")
        self.tree_detalle.grid(row = 10, column = 0, sticky="SWE",columnspan=5,padx = 10, pady = 10)
        
        # cantidad de producto
        total_etiqueta = ttk.Label(self, text='Total :', font=("Arial", 15))
        total_etiqueta.place(x= 750 , y=663)
        self.total_entrada = ttk.Entry(self)
        self.total_entrada.grid(row = 11, column=1, sticky='E',padx=10, pady=10)
        self.total_entrada.state(["readonly"])
        
        #Aceptar
        ttk.Style().configure("TButton", padding=6, relief="flat",background="#ccc")
        aceptar_boton = ttk.Button(self, text='Aceptar',command=self.aceptar)
        aceptar_boton.grid(row=12, column=1,sticky='E', padx=100, pady=20)
        #Cancelar
        cancelar_boton = ttk.Button(self, text='Cancelar',command=self.cancelar)
        cancelar_boton.grid(row=12, column=1,sticky='E', padx=10, pady=20)

    def agregar(self):
        self.id_tree_detalle = self.id_tree_detalle + 1
        producto = self.producto_entrada.get().split("_")
        cantidad = self.cantidad_entrada.get()
        subtotal = float(producto[3]) * int(cantidad)
        self.tree_detalle.insert("", tk.END, values=(self.id_tree_detalle,f"{producto[0]}_{producto[2]}",cantidad,subtotal))
        self.total = self.total + subtotal
        self.total_entrada.state(["!readonly"])
        self.total_entrada.delete(0, 'end')
        self.total_entrada.insert(0,self.total)
        self.total_entrada.state(["readonly"])
        
        
    def add_product_combobox(self,event):
        self.producto_entrada.set("")
        categoria = self.categoria_entrada.get().split("_")
        producto = Producto()
        productos = producto.select_producto(categoria[0])
        val_productos = []
        for prod in productos :
            producto_value = "_".join(str(v) for v in prod)
            val_productos.append(producto_value)
        self.producto_entrada['values'] = val_productos
        
    def aceptar(self):
        cliente = self.cliente_entrada.get().split()[0]
        tipo_comprobante = self.comprobante_entrada.get()
        numero_comprobante = self.nro_comprobante_entrada.get()
        fecha = self.fecha_entrada.get()
        total = self.total_entrada.get()
        detalles = []

        for line in self.tree_detalle.get_children():
            detalle_value = self.tree_detalle.item(line)
            id_producto = detalle_value["values"][1].split("_")[0]
            cantidad = int(detalle_value["values"][2])
            subtotal = float(detalle_value["values"][3])
            detalle = DetalleVenta(id_producto,cantidad,subtotal)
            detalles.append(detalle)

        venta = Venta(cliente,tipo_comprobante,numero_comprobante,
                          fecha,total,detalles)
        venta.crearVenta()
        self.refresh()

    def cancelar(self):
        self.destroy()

    def refresh(self):
        self.destroy()
        self.master.destroy()
        self.master = principal.Main()
        self.master.btnInfo2.invoke()
        self.master.mainloop()

if __name__ == '__main__':
    app = FormVenta()
    app.mainloop()