from src.DataBase.logicaBD import *
class Logica:
    def __init__(self, nombre, contraseña):
        self.nombre = nombre
        self.contraseña = contraseña

    def validarLogin(self):
        c = BaseDeDatos()
        if c.buscarUsuario(self.nombre,self.contraseña):
            return True
        return False
    
    def validarContraseña(self,contraseñaSegunda):
        if self.nombre != "":
            if self.contraseña != "":
                if self.contraseña == contraseñaSegunda:
                    c = BaseDeDatos()
                    c.agregarUsuario(self.nombre,self.contraseña)
                    return True
        return False
    
    def validarUserBD(self):
        c = BaseDeDatos()
        if c.buscarNombre(self.nombre):
            return True
        return False
    
    def cambiarContraseñaBD(self,contraseñaSegunda):
        if self.contraseña != "":
            if self.contraseña == contraseñaSegunda:
                c = BaseDeDatos()
                c.ActualizarContraseña(self.nombre,self.contraseña)
                return True
        return False