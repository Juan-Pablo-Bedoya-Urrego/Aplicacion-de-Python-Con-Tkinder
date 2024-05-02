from tkinter import ttk,messagebox, Menu
import tkinter as tk
from src.logica.logicaVehiculos import *

def ventanaVer():
    x = logicaGuardar("","","")
    vetadas = x.verVetadas()
    ventana = tk.Tk()
    ventana.geometry("400x250")
    ventana.title("Ver vetadas")

    laberTitulo = ttk.Label(ventana, text= "Lista placas vetadas")
    laberTitulo.pack()

    labelVetada = ttk.Label(ventana, text= "")
    labelVetada.pack()

    textoLista = '\n'.join(vetadas)
    labelVetada.config(text=textoLista)

    ventana.mainloop()