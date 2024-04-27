from tkinter import ttk,messagebox, Menu
import tkinter as tk
from logica import Logica
from ventanaPrincipal import *
import ventanaRegistro

ventana = None
intento = 0

def Registro():
    ventana.destroy()
    ventanaRegistro.ventanaRegistro()

def login():
    global intento
    intento += 1
    # Aquí se asume que tienes una clase Logica que está correctamente implementada
    x = Logica(entradaNombre.get(), entradaContraseña.get())
    if x.validarLogin():
        messagebox.showinfo("Exito","Inicio de sesión exitoso")
        ventana.destroy()
        principal()
    else:
        if intento >= 3:
            messagebox.showerror("Error", "Número máximo de intentos alcanzado")
            ventana.destroy()
        else:
            messagebox.showwarning("Intentos", f"Quedan {3 - intento} intentos")

# Crear la ventana
def ventanaLogin():
    global entradaNombre, entradaContraseña, ventana
    ventana = tk.Tk()
    ventana.geometry("250x250")
    ventana.title("Login")

    # Crear y posicionar los widgets
    labelNombre = ttk.Label(ventana, text="User: ")
    labelNombre.grid(row=0, column=0, padx=(30, 0), pady=5)

    entradaNombre = ttk.Entry(ventana, width=18, justify=tk.LEFT)
    entradaNombre.grid(row=0, column=1, padx=0, pady=5)

    labelContraseña = ttk.Label(ventana, text="Password: ")
    labelContraseña.grid(row=1, column=0, padx=(30, 0), pady=5)

    entradaContraseña = ttk.Entry(ventana, width=18, justify=tk.LEFT)
    entradaContraseña.grid(row=1, column=1, padx=0, pady=5)

    botonLogin = ttk.Button(ventana, text="Enter", command=login)
    botonLogin.grid(row=2, column=0, padx=(30, 0), pady=5)

    botonRegistro = ttk.Button(ventana, text="Registro" , command=Registro)
    botonRegistro.grid(row=2, column=1, padx=(30, 0), pady=5)

    ventana.mainloop()