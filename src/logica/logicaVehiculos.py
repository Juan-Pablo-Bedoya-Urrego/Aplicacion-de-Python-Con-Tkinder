from src.DataBase.logicaBD import *
class logicaGuardar:
    def __init__(self,nombre,placa,tipoVehiculo):
        self.nombre = nombre
        self.placa = placa
        self.tipo = tipoVehiculo

    def guardarVehiculo(self):
        c = BaseDeDatos()
        placasVetadas = c.retornarVetadas()
        for placaVetada in placasVetadas:
            if self.placa == placaVetada: 
                return True
        c.agregarVehiculo(self.placa,self.nombre,self.tipo)
        return False

    def agregarVetadas(self):
        c = BaseDeDatos()
        placasVetadas = c.retornarVetadas()
        for placaVetada in placasVetadas:
            if placaVetada == self.placa:
                return True
        c.agregarVeto(self.placa)
        return False

    def quitarVeto(self):
        c = BaseDeDatos()
        placasVetadas = c.retornarVetadas()
        for placaVetada in placasVetadas:
            if placaVetada == self.placa:
                c.deleteVeto(self.placa)
                return True
        return False
    
    def eliminarVehiculo(self):
        c = BaseDeDatos()
        if c.eliminarVehiculo(self.placa,self.tipo):
            return True
        return False
    
    def buscarVehiculo(self):
        c = BaseDeDatos
        c.buscarVehiculo(self.placa,self.tipo)
    
    def verVetadas(self):
        c = BaseDeDatos()
        placasVetadas = c.retornarVetadas()
        return placasVetadas