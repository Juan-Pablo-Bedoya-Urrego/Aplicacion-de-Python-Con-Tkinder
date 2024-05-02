from tkinter import ttk,messagebox, Menu
import tkinter as tk
import src.ventanas.ventanaAgregarVehiculo as ventanaAgregarVehiculo
import src.ventanas.ventanaVetar as ventanaVetar
import src.ventanas.ventanaEliminarVehiculo as ventanaEliminarVehiculo

def eliminarVehiculo():
    ventana.destroy()
    ventanaEliminarVehiculo.ventanaEliminar()

def AgregarVehiculo():
    ventana.destroy()
    ventanaAgregarVehiculo.ventanaVehiculo()

def vetadas():
    ventana.destroy()
    ventanaVetar.ventanaVetarPlacas()

def principal():
    global ventana
    ventana = tk.Tk()
    ventana.geometry("250x250")
    ventana.title("Principal")

    menu = Menu(ventana)
    subMenuAgregar = Menu(menu,tearoff=0)

    menu.add_cascade(menu=subMenuAgregar,label='Agregar vehiculo')
    subMenuAgregar.add_command(label='Agregar vehiculo',command= AgregarVehiculo)
    subMenuAgregar.add_command(label='eliminar',command= eliminarVehiculo)
    subMenuAgregar.add_command(label='Vetar',command= vetadas)

    ventana.config(menu=menu)
    ventana.mainloop()