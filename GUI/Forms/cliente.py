import tkinter as tk
from tkinter import ttk,Toplevel,Label
from tkinter import messagebox

class FormCliente(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Formulario Cliente")
        self.geometry("680x800")
        self.iconbitmap('GUI/image/icons/tienda.ico')
        self.resizable(0,0)
        # configuración del grid
        #self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self._create_label_input()

    def _create_label_input(self):

        # apellido
        apellido_etiqueta = ttk.Label(self, text='Apellido:')
        apellido_etiqueta.grid(row=1, column=0, sticky='W',padx=5, pady=5)
        self.apellido_entrada = ttk.Entry(self)
        self.apellido_entrada.grid(row=1, column=1, sticky='EW',padx=5, pady=5)

        # nombre
        nombre_etiqueta = ttk.Label(self, text='Nombre:')
        nombre_etiqueta.grid(row=1, column=0, sticky='W', padx=5, pady=5)
        self.nombre_entrada = ttk.Entry(self)
        self.nombre_entrada.grid(row=1, column=1, sticky='EW', padx=5, pady=5)

        # DNI
        dni_etiqueta = ttk.Label(self, text='Documento:')
        dni_etiqueta.grid(row=2, column=0, sticky='W',padx=5, pady=5)
        self.dni_entrada = ttk.Entry(self)
        self.dni_entrada.grid(row=2, column=1, sticky='EW',padx=5, pady=5)

        # Direccion
        direccion_etiqueta = ttk.Label(self, text='Direccion:')
        direccion_etiqueta.grid(row=3, column=0, sticky='W', padx=5, pady=5)
        self.direccion_entrada = ttk.Entry(self)
        self.direccion_entrada.grid(row=3, column=1, sticky='EW', padx=5, pady=5)

        # Fecha Nacimiento
        fecha_nacimiento_etiqueta = ttk.Label(self, text='Fecha Nacimiento:')
        fecha_nacimiento_etiqueta.grid(row=4, column=0, sticky='W', padx=5, pady=5)
        self.fecha_nacimiento_entrada = ttk.Entry(self)
        self.fecha_nacimiento_entrada.grid(row=4, column=1, sticky='EW', padx=5, pady=5)

        # Telefono
        telefono_etiqueta = ttk.Label(self, text='Telefono:')
        telefono_etiqueta.grid(row=5, column=0, sticky='W',padx=5, pady=5)
        self.telefono_entrada = ttk.Entry(self)
        self.telefono_entrada.grid(row=5, column=1, sticky='EW',padx=5, pady=5)

        # Email
        email_etiqueta = ttk.Label(self, text='Email:')
        email_etiqueta.grid(row=6, column=0, sticky='W', padx=5, pady=5)
        self.email_entrada = ttk.Entry(self)
        self.email_entrada.grid(row=6, column=1, sticky='EW', padx=5, pady=5)

        # Tipo de responsabilidad
        tipo_responsabilidad_etiqueta = ttk.Label(self, text='Tipo Responsabilidad:')
        tipo_responsabilidad_etiqueta.grid(row=7, column=0, sticky='W', padx=5, pady=5)
        self.tipo_responsabilidad_entrada = ttk.Entry(self)
        self.tipo_responsabilidad_entrada.grid(row=7, column=1, sticky='EW', padx=5, pady=5)

        # boton Login
        login_boton = ttk.Button(self, text='Login')
        login_boton.grid(row=8, column=0, columnspan=2)

    def aceptar(self):
        self.guardar = True
        self.padre.destroy()

    def cancelar(self):
        self.padre.destroy()

if __name__ == '__main__':
    app = FormCliente()
    app.mainloop()