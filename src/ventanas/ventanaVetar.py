from tkinter import ttk,messagebox, Menu
import tkinter as tk
from src.logica.logicaVehiculos import *

def realizarVeto():
    x = logicaGuardar("",entradaPlaca.get(),"")
    if x.agregarVetadas():
        messagebox.showwarning('Veto' , 'El vehiculo ya se encuentra vetado')
        entradaPlaca.delete(0, tk.END)
    else:
        messagebox.showinfo('Veto', 'veto realizado')

def ventanaVetarPlacas():
    global ventana, labelVetar, labelDesvetar, botonRealizarVeto, botonRealizardesveto, entradaPlaca, labelPlaca, botonSalir

    ventana = tk.Tk()
    ventana.geometry("400x250")
    ventana.title("Vetar placas")

    labelVetar = ttk.Label(ventana, text= "Vetar")
    labelVetar.grid(row=1, column=1, padx=(100,0), pady=(10,10))

    labelPlaca = ttk.Label(ventana, text="Placa: ")
    labelPlaca.grid(row=2, column=0, padx=(30, 0), pady=(0,30))

    entradaPlaca = ttk.Entry(ventana, width=18, justify=tk.LEFT)
    entradaPlaca.grid(row=2, column=1, padx=0, pady=(0,30))

    botonRealizarVeto = ttk.Button(ventana, width= 25, text= "Realizar veto de vehiculo", command= realizarVeto)
    botonRealizarVeto.grid(row=2, column=2, padx=0, pady=(0,30))
    
    ventana.mainloop()