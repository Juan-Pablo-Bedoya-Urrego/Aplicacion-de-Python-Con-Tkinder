from tkinter import ttk,messagebox, Menu
import tkinter as tk
from src.logica.logica import *
import src.ventanas.ventanaRegistro as ventanaRegistro 
import src.ventanas.ventanaLogin as ventanaLogin

def vRegistro():
    ventana.destroy()
    ventanaRegistro.ventanaRegistro()

def actualizarContraseña():
    x = Logica(entradaNombre.get(),entradaContraseña.get())
    if x.cambiarContraseñaBD(entradaContraseñaConfirmar.get()):
        x.cambiarContraseñaBD(entradaContraseña.get())
        messagebox.showinfo("Exitoso", "cambio de contraseña exitoso")
        ventana.destroy()
        ventanaLogin.ventanaLogin()
    else:
        messagebox.showwarning("Advertencia", "Las contraseñas no coinciden")

def validarUser():
    x = Logica(entradaNombre.get(),"")
    if x.validarUserBD():
        print("se encontro")
        global entradaContraseña, entradaContraseñaConfirmar
        
        botonValidarUsuario.grid_forget()
        botonRegistrarse.grid_forget()

        labelContraseña = ttk.Label(ventana, text="Password: ")
        labelContraseña.grid(row=1, column=0, padx=(30, 0), pady=5)

        entradaContraseña = ttk.Entry(ventana, width=18, justify=tk.LEFT)
        entradaContraseña.grid(row=1, column=1, padx=0, pady=5)

        labelContraseña = ttk.Label(ventana, text="Confirm Password: ")
        labelContraseña.grid(row=2, column=0, padx=(30, 0), pady=5)

        entradaContraseñaConfirmar = ttk.Entry(ventana, width=18, justify=tk.LEFT)
        entradaContraseñaConfirmar.grid(row=2, column=1, padx=0, pady=5)

        botonGuardar = ttk.Button(ventana, width=18, text="Guardar Contraseña", command= actualizarContraseña)
        botonGuardar.grid(row=3, column=1, padx=(0, 0), pady=5)
    else:
        print("never papa")
        botonRegistrarse.grid(row=2, column=1, padx=(0, 0), pady=5)


def ventanaCambio():
    global ventana, entradaNombre, botonValidarUsuario, botonRegistrarse
    ventana = tk.Tk()
    ventana.geometry("300x250")
    ventana.title("Cambio Contraseña")

    labelNombre = ttk.Label(ventana, text="User: ")
    labelNombre.grid(row=0, column=0, padx=(30, 0), pady=5)

    entradaNombre = ttk.Entry(ventana, width=18, justify=tk.LEFT)
    entradaNombre.grid(row=0, column=1, padx=0, pady=5)

    botonValidarUsuario = ttk.Button(ventana, width=18, text="Validar Usuario", command= validarUser)
    botonValidarUsuario.grid(row=1, column=1, padx=(0, 0), pady=5)

    
    botonRegistrarse = ttk.Button(ventana, width=18, text="Registrarse", command= vRegistro)
    botonRegistrarse.grid(row=2, column=1, padx=(0, 0), pady=5)
    botonRegistrarse.grid_forget()

    ventana.mainloop()
