from tkinter import ttk,messagebox, Menu
import tkinter as tk
from src.logica.logicaVehiculos import *

def Buscar():
    x = logicaGuardar("",entradaPlaca.get(),variableOpcion.get())
    x.buscarVehiculo()
    entradaPlaca.delete(0, tk.END)

def ventanaBuscarVehiculo():    
    global ventana, entradaNombre, entradaPlaca, variableOpcion
    ventana = tk.Tk()
    ventana.geometry("300x250")
    ventana.title("Buscar Vehiculo")

    labelNombre = ttk.Label(ventana, text="Placa: ")
    labelNombre.grid(row=0, column=0, padx=(30, 0), pady=5)

    entradaPlaca = ttk.Entry(ventana, width=18, justify=tk.LEFT)
    entradaPlaca.grid(row=0, column=1, padx=0, pady=5)

    labelSeleccion = tk.Label(ventana, text="Selecciona una opción: ")
    labelSeleccion.grid(row=1, column=0, padx=(30, 0), pady=5)

    opciones = ["Moto", "Carro"]
    variableOpcion = tk.StringVar(ventana)
    variableOpcion.set(opciones[0])

    menu_desplegable = tk.OptionMenu(ventana, variableOpcion, *opciones)
    menu_desplegable.grid(row=1, column=1, padx=0, pady=5)

    botonGuardar = ttk.Button(ventana, width=18, text="Buscar", command=Buscar)
    botonGuardar.grid(row=2, column=1, padx=(0, 0), pady=5)