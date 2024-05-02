from tkinter import ttk,messagebox, Menu
import tkinter as tk
from src.logica.logicaVehiculos import *
import src.ventanas.ventanaPrincipal as ventanaPincipal

def eliminarVehiculo():
    x = logicaGuardar("",entradaPlaca.get(),variableOpcion.get())
    if x.eliminarVehiculo():
        messagebox.showinfo('Eliminar' , f'La {variableOpcion.get()} se elimino correctamente')
    else:
        messagebox.showwarning('Advertencia' , 'Verificaque el tipo de vehiculo o la placa es mal escrita')

def ventanaP():
    ventana.destroy()
    ventanaPincipal.principal()

def ventanaEliminar():
    global ventana, entradaPlaca, variableOpcion
    ventana = tk.Tk()
    ventana.geometry("400x250")
    ventana.title("Eliminar vehiculo")

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

    botonEliminar = ttk.Button(ventana, width= 18, text= "Eliminar", command= eliminarVehiculo)
    botonEliminar.grid(row=2, column=1, padx=(0, 0), pady=5)

    botonSalir = ttk.Button(ventana, width=18, text="salir", command=ventanaP)
    botonSalir.grid(row=4, column=0, padx=(0, 0), pady=70)

    ventana.mainloop()

ventanaEliminar()