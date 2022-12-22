import tkinter as tk
from tkinter import ttk,Toplevel
from tkinter import messagebox

from GUI.Forms.form_cliente import FormCliente
from GUI.Forms.form_producto import FormProducto
from GUI.Forms.form_venta import FormVenta
from Sistema.Productos.producto import Producto
from Sistema.Venta.cliente import Cliente
from Sistema.Venta.venta import Venta

class Main(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Menu Principal")
        self.geometry("1080x900")
        self.iconbitmap('GUI/image/icons/tienda.ico')
        self.photo = tk.PhotoImage(file = r"GUI/image/img/cliente.png")
        self.photo1 = tk.PhotoImage(file = r"GUI/image/img/producto.png")
        self.photo2 = tk.PhotoImage(file = r"GUI/image/img/venta.png")
        self.photo4 = tk.PhotoImage(file = r"GUI/image/img/pdf.png")
        self.photo5 = tk.PhotoImage(file = r"GUI/image/img/info.png")
        self.img_create_person = tk.PhotoImage(file = r"GUI/image/img/add_persona.png")
        self.img_edit_person = tk.PhotoImage(file = r"GUI/image/img/editar_persona.png")
        self.img_delete_person = tk.PhotoImage(file = r"GUI/image/img/delete_persona.png")
        self.img_create_sale = tk.PhotoImage(file = r"GUI/image/img/create_venta.png")
        self.img_delete_sale = tk.PhotoImage(file = r"GUI/image/img/delete_venta.png")
        #self.resizable(False, False)
        self.columnconfigure(0, weight = 3)
        self.columnconfigure(1, weight = 3)
        self.columnconfigure(2, weight = 3)
        self.columnconfigure(3, weight = 3)
        self.columnconfigure(4, weight = 3)
        self._create_menu()
        self._create_boton_action()
        
    # Crear el menu   
    def _create_menu(self):
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)
        # Crear el menu de opciones
        opciones_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label='Opciones', menu=opciones_menu)
        #opciones_menu.add_command(label='Login', command=self._login)
        #opciones_menu.add_command(label='Salir', command=self.destroy)
        #opciones_menu.add_command(label='Login')
        opciones_menu.add_command(label='Salir')
        # Crear el menu de ayuda
        ayuda_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='Ayuda', menu=ayuda_menu)
        #ayuda_menu.add_command(label='Acerca de', command=self._acerca_de)
        ayuda_menu.add_command(label='Acerca de')

    
    def _create_boton_action(self):

        self.btnInfo = tk.Button(self, image = self.photo, width = 50, height = 50, command = self._list_client)
        btnInfo1 = tk.Button(self,  image = self.photo1, width=50, height=50,  command = self._list_producto)
        self.btnInfo2 = tk.Button(self, image =  self.photo2, width=50, height=50,  command = self._list_sale)
        btnInfo3 = tk.Button(self, image = self.photo4, width = 50, height = 50)
        btnInfo4 = tk.Button(self, image = self.photo5, width = 50, height = 50)

        self.btnInfo.grid(row = 1, column = 0, sticky="NWE")
        btnInfo1.grid(row = 1, column = 1, sticky="NWE")
        self.btnInfo2.grid(row = 1, column = 2, sticky="NWE")
        btnInfo3.grid(row = 1, column = 3, sticky="NWE")
        btnInfo4.grid(row = 1, column = 4, sticky="NWE")


    def _list_client(self):
        self.tree_cliente = ttk.Treeview(self, column=("c1", "c2", "c3","c4", "c5", "c6","c7","c8","c9","c10"), show='headings')
        self.tree_cliente.column("#1", anchor=tk.CENTER, minwidth = 4)
        self.tree_cliente.heading("#1", text="Nro")
        self.tree_cliente.column("#2", anchor=tk.CENTER)
        self.tree_cliente.heading("#2", text="Apellido")
        self.tree_cliente.column("#3", anchor=tk.CENTER)
        self.tree_cliente.heading("#3", text="Nombre")
        self.tree_cliente.column("#4", anchor=tk.CENTER)
        self.tree_cliente.heading("#4", text="Documento")
        self.tree_cliente.column("#5", anchor=tk.CENTER)
        self.tree_cliente.heading("#5", text="Domicilio")
        self.tree_cliente.column("#6", anchor=tk.CENTER)
        self.tree_cliente.heading("#6", text="FechaNac.")
        self.tree_cliente.column("#7", anchor=tk.CENTER)
        self.tree_cliente.heading("#7", text="Telefon")
        self.tree_cliente.column("#8", anchor=tk.CENTER)
        self.tree_cliente.heading("#8", text="Email")
        self.tree_cliente.column("#9", anchor=tk.CENTER)
        self.tree_cliente.heading("#9", text="Tipo")
        self.tree_cliente.column("#10", anchor=tk.CENTER)
        self.tree_cliente.heading("#10", text="Estado")
        cliente = Cliente()
        clientes = cliente.listarClientes()
        for cl in clientes:
            self.tree_cliente.insert("", tk.END, values=cl)
        self.tree_cliente.grid(row = 2, column = 0, sticky="SWE",columnspan=5,padx = 10, pady = 10)
        btn_create = tk.Button(self, image = self.img_create_person, width = 50, height = 50, command = self.form_client)
        btn_create.grid(row = 3, column = 0, sticky="SWE",padx = 10)
        btn_edit = tk.Button(self, image = self.img_edit_person, width = 50, height = 50, command = self.form_edit_client)
        btn_edit.grid(row = 3, column = 1, sticky="SWE",padx = 10)
        btn_delete = tk.Button(self, image = self.img_delete_person, width = 50, height = 50)
        btn_delete.grid(row = 3, column = 2, sticky="SWE",padx = 10) 
        
    def _list_sale(self):
        self.tree_sale = ttk.Treeview(self, column=("c1", "c2", "c3","c4","c5","c6","c7"), show='headings')
        self.tree_sale.column("#1", anchor=tk.CENTER)
        self.tree_sale.heading("#1", text="Nro")
        self.tree_sale.column("#2", anchor=tk.CENTER)
        self.tree_sale.heading("#2", text="Cliente")
        self.tree_sale.column("#3", anchor=tk.CENTER)
        self.tree_sale.heading("#3", text="Tipo Comprobante")
        self.tree_sale.column("#4", anchor=tk.CENTER)
        self.tree_sale.heading("#4", text="Nro Comprobante")
        self.tree_sale.column("#5", anchor=tk.CENTER)
        self.tree_sale.heading("#5", text="Fecha")
        self.tree_sale.column("#6", anchor=tk.CENTER)
        self.tree_sale.heading("#6", text="Total")
        self.tree_sale.column("#7", anchor=tk.CENTER)
        self.tree_sale.heading("#7", text="Estado")
        venta = Venta()
        ventas = venta.listar_venta()
        for vnt in ventas:
            self.tree_sale.insert("", tk.END, values=vnt)
        self.tree_sale.grid(row = 2, column = 0, sticky="SWE",columnspan=5,padx = 10, pady = 10)
        btn_create = tk.Button(self, image = self.img_create_sale, width = 50, height = 50, command = self.form_venta)
        btn_create.grid(row = 3, column = 0, sticky="SWE",padx = 10)
        btn_delete = tk.Button(self, image = self.img_delete_sale, width = 50, height = 50)
        btn_delete.grid(row = 3, column = 1, sticky="SWE",padx = 10) 
        

    def _list_producto(self):
        self.tree_producto = ttk.Treeview(self, column=("c1", "c2", "c3","c4","c5","c6","c7","c8"), show='headings')
        self.tree_producto.column("#1", anchor=tk.CENTER)
        self.tree_producto.heading("#1", text="Nro")
        self.tree_producto.column("#2", anchor=tk.CENTER)
        self.tree_producto.heading("#2", text="Categoria")
        self.tree_producto.column("#3", anchor=tk.CENTER)
        self.tree_producto.heading("#3", text="Codigo")
        self.tree_producto.column("#4", anchor=tk.CENTER)
        self.tree_producto.heading("#4", text="Nombre")
        self.tree_producto.column("#5", anchor=tk.CENTER)
        self.tree_producto.heading("#5", text="Stock")
        self.tree_producto.column("#6", anchor=tk.CENTER)
        self.tree_producto.heading("#6", text="Precio")
        self.tree_producto.heading("#7", text="Descripcion")
        self.tree_producto.column("#7", anchor=tk.CENTER)
        self.tree_producto.heading("#8", text="Estado")
        self.tree_producto.column("#8", anchor=tk.CENTER)
        self.tree_producto.grid(row = 2, column = 0, sticky="SWE",columnspan=5,padx = 10, pady = 10)
        producto = Producto()
        productos = producto.listar_producto()
        for pd in productos:
            self.tree_producto.insert("", tk.END, values=pd)
        self.tree_producto.grid(row = 2, column = 0, sticky="SWE",columnspan=5,padx = 10, pady = 10)
        btn_create = tk.Button(self, image = self.img_create_person, width = 50, height = 50, command = self.form_client)
        btn_create.grid(row = 3, column = 0, sticky="SWE",padx = 10)
        btn_edit = tk.Button(self, image = self.img_edit_person, width = 50, height = 50, command = self.form_edit_client)
        btn_edit.grid(row = 3, column = 1, sticky="SWE",padx = 10)
        btn_delete = tk.Button(self, image = self.img_delete_person, width = 50, height = 50)
        btn_delete.grid(row = 3, column = 2, sticky="SWE",padx = 10)

    def form_client(self):
        app = FormCliente(self)
        app.mainloop()
    
    def form_edit_client(self):
        curItem = self.tree_cliente.focus()
        cliente_form = self.tree_cliente.item(curItem)
        app = FormCliente(self)
        app.id_cliente_entrada.insert(0,cliente_form["values"][0])
        app.apellido_entrada.insert(0,cliente_form['values'][1])
        app.nombre_entrada.insert(0,cliente_form['values'][2])
        app.dni_entrada.insert(0,cliente_form['values'][3])
        app.direccion_entrada.insert(0,cliente_form['values'][4])
        app.fecha_nacimiento_entrada.insert(0,cliente_form['values'][5])
        app.telefono_entrada.insert(0,cliente_form['values'][6])
        app.email_entrada.insert(0,cliente_form['values'][7])
        app.tipo_responsabilidad_entrada.insert(0,cliente_form['values'][8])
        app.mainloop()
    
    def form_venta(self):
        app = FormVenta(self)
        app.mainloop()
    
    def form_producto(self):
        app = FormProducto(self)
        app.mainloop()

    def refresh(self):
        self.destroy()
        self.__init__()


if __name__ == '__main__':
    app = Main()
    app.mainloop()
