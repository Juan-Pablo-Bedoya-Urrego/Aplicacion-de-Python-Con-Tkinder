from tkinter import ttk,messagebox, Menu
import tkinter as tk
from src.logica.logicaVehiculos import *

def realizarDesveto():
    salir = messagebox.askquestion("Salir", "¿Desea desvetar el vehiculo?")
    if salir == "yes":    
        x = logicaGuardar("",entradaPlaca.get(),"")
        if x.quitarVeto():
            entradaPlaca.delete(0, tk.END)
        else:
            messagebox.showwarning('Veto', 'Placa no encontrada')

def ventanaDesvetarPlacas():
    global ventana, labelDesvetar, botonRealizarDesveto, entradaPlaca, labelPlaca

    ventana = tk.Tk()
    ventana.geometry("400x250")
    ventana.title("Desvetar placas")

    labelDesvetar = ttk.Label(ventana, text= "Desvetar")
    labelDesvetar.grid(row=1, column=1, padx=(100,0), pady=(10,10))

    labelPlaca = ttk.Label(ventana, text="Placa: ")
    labelPlaca.grid(row=2, column=0, padx=(30, 0), pady=(0,30))

    entradaPlaca = ttk.Entry(ventana, width=18, justify=tk.LEFT)
    entradaPlaca.grid(row=2, column=1, padx=0, pady=(0,30))

    botonRealizarDesveto = ttk.Button(ventana, width= 25, text= "Realizar desveto de vehiculo", command= realizarDesveto)
    botonRealizarDesveto.grid(row=2, column=2, padx=0, pady=(0,30))
    
    ventana.mainloop()