from tkinter import ttk,messagebox, Menu
import tkinter as tk
from src.logica.logicaVehiculos import logicaGuardar
import src.ventanas.ventanaPrincipal as ventanaPincipal

def guardarVehiculo():
    x = logicaGuardar(entradaNombre.get(),entradaPlaca.get(),variableOpcion.get())
    if x.guardarVehiculo():
        messagebox.showerror('Placa vetada', 'Su placa a sido vetada del parquiadero')
    else:
        messagebox.showinfo(f'{variableOpcion.get()} guardada' , f'Su {variableOpcion.get()} se guardo')

def ventanaP():
    ventana.destroy()
    ventanaPincipal.principal()

def ventanaVehiculo():
    global ventana, entradaNombre, entradaPlaca, variableOpcion
    ventana = tk.Tk()
    ventana.geometry("300x250")
    ventana.title("Cambio Contraseña")

    labelNombre = ttk.Label(ventana, text="Placa: ")
    labelNombre.grid(row=0, column=0, padx=(30, 0), pady=5)

    entradaPlaca = ttk.Entry(ventana, width=18, justify=tk.LEFT)
    entradaPlaca.grid(row=0, column=1, padx=0, pady=5)

    labelContraseña = ttk.Label(ventana, text="Nombre: ")
    labelContraseña.grid(row=1, column=0, padx=(30, 0), pady=5)

    entradaNombre = ttk.Entry(ventana, width=18, justify=tk.LEFT)
    entradaNombre.grid(row=1, column=1, padx=0, pady=5)

    labelSeleccion = tk.Label(ventana, text="Selecciona una opción: ")
    labelSeleccion.grid(row=2, column=0, padx=(30, 0), pady=5)

    opciones = ["Moto", "Carro"]
    variableOpcion = tk.StringVar(ventana)
    variableOpcion.set(opciones[0])

    menu_desplegable = tk.OptionMenu(ventana, variableOpcion, *opciones)
    menu_desplegable.grid(row=2, column=1, padx=0, pady=5)

    botonGuardar = ttk.Button(ventana, width=18, text="Guardar", command=guardarVehiculo)
    botonGuardar.grid(row=3, column=1, padx=(0, 0), pady=5)

    botonSalir = ttk.Button(ventana, width=18, text="salir", command=ventanaP)
    botonSalir.grid(row=4, column=0, padx=(0, 0), pady=70)
