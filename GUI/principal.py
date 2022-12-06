import tkinter as tk
from tkinter import ttk,Toplevel
from tkinter import messagebox

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

        btnInfo = tk.Button(self, image = self.photo, width = 50, height = 50, command = self._list_client)
        btnInfo1 = tk.Button(self,  image = self.photo1, width=50, height=50,  command = self._list_producto)
        btnInfo2 = tk.Button(self, image =  self.photo2, width=50, height=50,  command = self._list_sale)
        btnInfo3 = tk.Button(self, image = self.photo4, width = 50, height = 50)
        btnInfo4 = tk.Button(self, image = self.photo5, width = 50, height = 50)

        btnInfo.grid(row = 1, column = 0, sticky="NWE")
        btnInfo1.grid(row = 1, column = 1, sticky="NWE")
        btnInfo2.grid(row = 1, column = 2, sticky="NWE")
        btnInfo3.grid(row = 1, column = 3, sticky="NWE")
        btnInfo4.grid(row = 1, column = 4, sticky="NWE")


    def _list_client(self):
        tree = ttk.Treeview(self, column=("c1", "c2", "c3","c4"), show='headings')
        tree.column("#1", anchor=tk.CENTER)
        tree.heading("#1", text="Nro")
        tree.column("#2", anchor=tk.CENTER)
        tree.heading("#2", text="Apellido")
        tree.column("#3", anchor=tk.CENTER)
        tree.heading("#3", text="Nombre")
        tree.column("#4", anchor=tk.CENTER)
        tree.heading("#4", text="Documento")
        tree.column("#4", anchor=tk.CENTER)
        tree.heading("#4", text="Domicilio")
        tree.grid(row = 2, column = 0, sticky="SWE",columnspan=5,padx = 10, pady = 10)
        self.img_create_person = tk.PhotoImage(file = r"GUI/image/img/add_persona.png")
        self.img_edit_person = tk.PhotoImage(file = r"GUI/image/img/editar_persona.png")
        self.img_delete_person = tk.PhotoImage(file = r"GUI/image/img/delete_persona.png")
        btn_create = tk.Button(self, image = self.img_create_person, width = 50, height = 50)
        btn_create.grid(row = 3, column = 0, sticky="SWE",padx = 10)
        btn_create = tk.Button(self, image = self.img_edit_person, width = 50, height = 50)
        btn_create.grid(row = 3, column = 1, sticky="SWE",padx = 10)
        btn_create = tk.Button(self, image = self.img_delete_person, width = 50, height = 50)
        btn_create.grid(row = 3, column = 2, sticky="SWE",padx = 10)
    
    def _list_sale(self):
        tree = ttk.Treeview(self, column=("c1", "c2", "c3","c4"), show='headings')
        tree.column("#1", anchor=tk.CENTER)
        tree.heading("#1", text="Nro")
        tree.column("#2", anchor=tk.CENTER)
        tree.heading("#2", text="Cliente")
        tree.column("#3", anchor=tk.CENTER)
        tree.heading("#3", text="Fecha")
        tree.column("#4", anchor=tk.CENTER)
        tree.heading("#4", text="Total")
        tree.grid(row = 2, column = 0, sticky="SWE",columnspan=5,padx = 10, pady = 10)
        

    def _list_producto(self):
        tree = ttk.Treeview(self, column=("c1", "c2", "c3","c4"), show='headings')
        tree.column("#1", anchor=tk.CENTER)
        tree.heading("#1", text="Nro")
        tree.column("#2", anchor=tk.CENTER)
        tree.heading("#2", text="Nombre")
        tree.column("#3", anchor=tk.CENTER)
        tree.heading("#3", text="Stock")
        tree.column("#4", anchor=tk.CENTER)
        tree.heading("#4", text="Precio")
        tree.grid(row = 2, column = 0, sticky="SWE",columnspan=5,padx = 10, pady = 10)
        
if __name__ == '__main__':
    app = Main()
    app.mainloop()