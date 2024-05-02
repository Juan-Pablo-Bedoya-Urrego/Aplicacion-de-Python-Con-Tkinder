from datetime import datetime
import os
from tkinter import ttk,messagebox

class crearRecivos:
    def __init__(self,nombre,placa,tipo):
        fechaHora = datetime.now()
        self.nombre = nombre
        self.placa = placa
        self.tipo = tipo
        self.hora = fechaHora.time()
        self.dia = fechaHora.date()

    def crear(self):
        contenido = (f"El vehiculo tipo {self.tipo} con placas {self.placa} \n ",
                f"entro el dia: {self.dia} a las: {self.hora}.\n",
                f"Propietario: {self.nombre}")
        try:
            with open(f"Recibo {self.placa}.txt", "w") as archivo:
                archivo.write(''.join(contenido))
                messagebox.showinfo('creacion recibo', 'El recibo de entrada se creó correctamente')
        except Exception as e:
            print(e)

    def eliminar(self):
        archivo = f"Recibo {self.placa}.txt"
        if os.path.exists(archivo):
            os.remove(archivo)
            messagebox.showinfo('Eliminacion', 'El recibo se borro correctamente')