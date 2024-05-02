from tkinter import ttk,messagebox, Menu
import tkinter as tk
import src.ventanas.ventanaAgregarVehiculo as ventanaAgregarVehiculo
import src.ventanas.ventanaVetar as ventanaVetar
import src.ventanas.ventanaEliminarVehiculo as ventanaEliminarVehiculo
import src.ventanas.ventanaDesvetar as ventanaDesvetar 
import src.ventanas.ventanaBuscar as ventanaBuscar
import src.ventanas.ventanaVerVetada as ventanaVerVetada

def eliminarVehiculo():
    ventanaEliminarVehiculo.ventanaEliminar()

def AgregarVehiculo():
    ventanaAgregarVehiculo.ventanaVehiculo()

def vetadas():
    ventanaVetar.ventanaVetarPlacas()

def desvetadas():
    ventanaDesvetar.ventanaDesvetarPlacas()

def buscarVehiculo():
    ventanaBuscar.ventanaBuscarVehiculo()

def verLista():
    ventanaVerVetada.ventanaVer()

def salir():
        salir = messagebox.askquestion("Salir", "¿Desea salir?")
        if salir == "yes":
            ventana.quit()
            ventana.destroy()

def principal():
    global ventana
    ventana = tk.Tk()
    ventana.geometry("250x250")
    ventana.title("Principal")
    menu = Menu(ventana)
    ventana.config(menu=menu)

    Vehiculo = Menu(menu, tearoff=0)
    Vehiculo.add_command(label="Agregar", command=AgregarVehiculo)
    Vehiculo.add_command(label="Eliminar", command=eliminarVehiculo)
    Vehiculo.add_command(label="Buscar", command=buscarVehiculo)
    Vehiculo.add_separator()
    Vehiculo.add_command(label="Exit", command=salir)

    Vetos = Menu(menu, tearoff=0)
    Vetos.add_command(label="Vetar",  command=vetadas)
    Vetos.add_command(label="Desvetar", command=desvetadas)
    Vetos.add_command(label="Ver lista de vetados", command=verLista)
    Vetos.add_separator()
    Vetos.add_command(label="About")
    menu.add_cascade(label="Vehiculos", menu=Vehiculo)
    menu.add_cascade(label="Vetar & Desvetar", menu=Vetos)

    ventana.config(menu=menu)
    ventana.mainloop()