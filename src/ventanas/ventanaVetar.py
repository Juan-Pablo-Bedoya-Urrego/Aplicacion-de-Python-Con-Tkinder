from tkinter import ttk,messagebox, Menu
import tkinter as tk
from src.logica.logicaVehiculos import *
import src.ventanas.ventanaPrincipal as ventanaPincipal

def ventanaP():
    ventana.destroy()
    ventanaPincipal.principal()

def realizarVeto():
    x = logicaGuardar("",entradaPlaca.get(),"")
    if x.agregarVetadas():
        messagebox.showwarning('Veto' , 'El vehiculo ya se encuentra vetado')
    else:
        messagebox.showinfo('Veto', 'veto realizado')

def realizarDesveto():
    x = logicaGuardar("",entradaPlaca.get(),"")
    if x.quitarVeto():
        messagebox.showinfo('Veto', 'Veto quitado')
    else:
        messagebox.showwarning('Veto', 'Placa no encontrada')

def vetar():
    botonRealizardesveto.grid_forget()
    labelDesvetar.grid_forget()
    labelPlaca.grid_forget()
    entradaPlaca.grid_forget()
    labelVetar.grid(row=1, column=1, padx=(100,0), pady=(10,10))
    botonRealizarVeto.grid(row=2, column=2, padx=0, pady=(0,30))
    entradaPlaca.grid(row=2, column=1, padx=0, pady=(0,30))
    labelPlaca.grid(row=2, column=0, padx=(30, 0), pady=(0,30))

def desvetar():
    botonRealizarVeto.grid_forget()
    labelVetar.grid_forget()
    labelPlaca.grid_forget()
    entradaPlaca.grid_forget()
    labelDesvetar.grid(row=1, column=1, padx=(100,0), pady=(10,10))
    botonRealizardesveto.grid(row=2, column=2, padx=0, pady=(0,30))
    entradaPlaca.grid(row=2, column=1, padx=0, pady=(0,30))
    labelPlaca.grid(row=2, column=0, padx=(30, 0), pady=(0,30))

def ventanaVetarPlacas():
    global ventana, labelVetar, labelDesvetar, botonRealizarVeto, botonRealizardesveto, entradaPlaca, labelPlaca, botonSalir

    ventana = tk.Tk()
    ventana.geometry("400x250")
    ventana.title("Vetar placas")

    botonVetar = ttk.Button(ventana,width=18, text="vetar vehiculo", command= vetar)
    botonVetar.grid(row=0, column=1, padx=(35,0), pady=5)

    botonDesvetar = ttk.Button(ventana, width= 18, text= "desvetar vehiculo", command= desvetar)
    botonDesvetar.grid(row=0, column=2, padx=(35,0), pady=5)

    labelVetar = ttk.Label(ventana, text= "Ventar")
    labelDesvetar = ttk.Label(ventana, text= "Desvetar")

    labelPlaca = ttk.Label(ventana, text="Placa: ")
    entradaPlaca = ttk.Entry(ventana, width=18, justify=tk.LEFT)
    botonRealizarVeto = ttk.Button(ventana, width= 25, text= "Realizar veto de vehiculo", command= realizarVeto)
    botonRealizardesveto = ttk.Button(ventana, width=25, text= "Realizar desveto de vehiculo",command= realizarDesveto)

    botonSalir = ttk.Button(ventana, width=18, text="salir", command=ventanaP)
    botonSalir.grid(row=4, column=1, padx=(35,0), pady=70)

    ventana.mainloop()
