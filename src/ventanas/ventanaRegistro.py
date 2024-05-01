from tkinter import ttk,messagebox, Menu
import tkinter as tk
from src.logica.logica import *
import src.ventanas.ventanaLogin as ventanaLogin

def confirmarRegistro():
    c = Logica(entradaNombre.get(), entradaContraseña.get())
    if not c.validarUserBD():
        if c.validarContraseña(entradaContraseñaConfirmar.get()):
            messagebox.showinfo("Creacion","Usuario registrado con exito")
            ventana.destroy()
            ventanaLogin.ventanaLogin()
        else:
            messagebox.showerror("Error" , "Las contraseñas no coinciden o los datos no pueden estar vacios")
    else:
        messagebox.showerror("Error", "El usuario ya existe")


def ventanaRegistro():
    global entradaNombre, entradaContraseña, entradaContraseñaConfirmar, ventana
    ventana = tk.Tk() 
    ventana.geometry("310x250")
    ventana.title("Login Celador")

    labelNombre = ttk.Label(ventana, text="User: ")
    labelNombre.grid(row=0, column=0, padx=(30, 0), pady=5)

    entradaNombre = ttk.Entry(ventana, width=18, justify=tk.LEFT)
    entradaNombre.grid(row=0, column=1, padx=0, pady=5)

    labelContraseña = ttk.Label(ventana, text="Password: ")
    labelContraseña.grid(row=1, column=0, padx=(30, 0), pady=5)

    entradaContraseña = ttk.Entry(ventana, width=18, justify=tk.LEFT)
    entradaContraseña.grid(row=1, column=1, padx=0, pady=5)

    labelContraseña = ttk.Label(ventana, text="Confirm Password: ")
    labelContraseña.grid(row=2, column=0, padx=(30, 0), pady=5)

    entradaContraseñaConfirmar = ttk.Entry(ventana, width=18, justify=tk.LEFT)
    entradaContraseñaConfirmar.grid(row=2, column=1, padx=0, pady=5)

    botonLogin = ttk.Button(ventana, text="          Registrar          ", command= confirmarRegistro)
    botonLogin.grid(row=3, column=1, padx=(0, 0), pady=5)

    ventana.mainloop()