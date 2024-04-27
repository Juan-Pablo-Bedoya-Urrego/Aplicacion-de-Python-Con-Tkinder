from logicaBD import *
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
        if not self.nombre == "":
            if self.contraseña == contraseñaSegunda:
                c = BaseDeDatos()
                c.agregarUsuario(self.nombre,self.contraseña)
                return True
        return False
