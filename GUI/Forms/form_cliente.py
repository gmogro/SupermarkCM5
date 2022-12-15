import tkinter as tk
from tkinter import ttk,Toplevel,Label
from tkinter import messagebox
from tkcalendar import DateEntry

from Sistema.Venta.cliente import Cliente

class FormCliente(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Crear Cliente")
        self.geometry("680x500")
        self.iconbitmap('GUI/image/icons/tienda.ico')
        self.resizable(0,0)
        self.columnconfigure(1, weight=2)
        self._create_label_input()

    def _create_label_input(self):

        form_etiqueta = ttk.Label(self, text='Crear Cliente', font=("Arial", 25))
        form_etiqueta.grid(row=0, column=0, columnspan=2,padx=20, pady=20)

        # apellido
        apellido_etiqueta = ttk.Label(self, text='Apellido:')
        apellido_etiqueta.grid(row=1, column=0, sticky='W',padx=5, pady=10)
        self.apellido_entrada = ttk.Entry(self)
        self.apellido_entrada.grid(row=1, column=1, sticky='EW',padx=5, pady=10)

        # nombre
        nombre_etiqueta = ttk.Label(self, text='Nombre:')
        nombre_etiqueta.grid(row=2, column=0, sticky='W', padx=5, pady=10)
        self.nombre_entrada = ttk.Entry(self)
        self.nombre_entrada.grid(row=2, column=1, sticky='EW', padx=5, pady=10)

        # DNI
        dni_etiqueta = ttk.Label(self, text='Documento:')
        dni_etiqueta.grid(row=3, column=0, sticky='W',padx=5, pady=10)
        self.dni_entrada = ttk.Entry(self)
        self.dni_entrada.grid(row=3, column=1, sticky='EW',padx=5, pady=10)

        # Direccion
        direccion_etiqueta = ttk.Label(self, text='Direccion:')
        direccion_etiqueta.grid(row=4, column=0, sticky='W', padx=5, pady=10)
        self.direccion_entrada = ttk.Entry(self)
        self.direccion_entrada.grid(row=4, column=1, sticky='EW', padx=5, pady=10)

        # Fecha Nacimiento
        fecha_nacimiento_etiqueta = ttk.Label(self, text='Fecha Nacimiento:')
        fecha_nacimiento_etiqueta.grid(row=5, column=0, sticky='W', padx=5, pady=10)
        #self.fecha_nacimiento_entrada = DateEntry(self)
        self.fecha_nacimiento_entrada = ttk.Entry(self)
        self.fecha_nacimiento_entrada.grid(row=5, column=1, sticky='EW', padx=5, pady=10)

        # Telefono
        telefono_etiqueta = ttk.Label(self, text='Telefono:')
        telefono_etiqueta.grid(row=6, column=0, sticky='W',padx=5, pady=10)
        self.telefono_entrada = ttk.Entry(self)
        self.telefono_entrada.grid(row=6, column=1, sticky='EW',padx=5, pady=10)

        # Email
        email_etiqueta = ttk.Label(self, text='Email:')
        email_etiqueta.grid(row=7, column=0, sticky='W', padx=5, pady=10)
        self.email_entrada = ttk.Entry(self)
        self.email_entrada.grid(row=7, column=1, sticky='EW', padx=5, pady=10)

        # Tipo de responsabilidad
        tipo_responsabilidad_etiqueta = ttk.Label(self, text='Tipo Responsabilidad:')
        tipo_responsabilidad_etiqueta.grid(row=8, column=0, sticky='W', padx=5, pady=10)
        self.tipo_responsabilidad_entrada = ttk.Combobox(self,values=['Monotributista','Responsable Inscripto','Cosumidor Final'])
        self.tipo_responsabilidad_entrada.grid(row=8, column=1, sticky='EW', padx=5, pady=10)
        
        #id_cliente
        self.id_cliente_entrada = ttk.Entry(self)
        self.id_cliente_entrada.grid(row=9, column=1, sticky='EW', padx=5, pady=10)

        #Aceptar
        ttk.Style().configure("TButton", padding=6, relief="flat",background="#ccc")
        aceptar_boton = ttk.Button(self, text='Aceptar',command=self.aceptar)
        aceptar_boton.grid(row=10, column=1,sticky='E', padx=100, pady=20)
        #Cancelar
        cancelar_boton = ttk.Button(self, text='Cancelar',command=self.cancelar)
        cancelar_boton.grid(row=10, column=1,sticky='E', padx=5, pady=20)

    def aceptar(self):
        if self.id_cliente_entrada.get() == "":
            cliente = Cliente(self.nombre_entrada.get(),self.apellido_entrada.get(),self.direccion_entrada.get(),
                            self.telefono_entrada.get(),self.fecha_nacimiento_entrada.get(),
                            self.dni_entrada.get(),self.email_entrada.get(),self.tipo_responsabilidad_entrada.get())
            cliente.crearCliente()
        else:
            cliente = Cliente(self.nombre_entrada.get(),self.apellido_entrada.get(),self.direccion_entrada.get(),
                            self.telefono_entrada.get(),self.fecha_nacimiento_entrada.get(),
                            self.dni_entrada.get(),self.email_entrada.get(),self.tipo_responsabilidad_entrada.get(),
                            self.id_cliente_entrada.get())
            cliente.modificarCliente()
        self.destroy()

    def cancelar(self):
        self.destroy()
