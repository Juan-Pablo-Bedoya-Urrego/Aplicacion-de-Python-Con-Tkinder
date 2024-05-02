from datetime import datetime
class crearRecivos:
    def __init__(self,nombre,placa):
        fechaHora = datetime.now()
        self.nombre = nombre
        self.placa = placa
        self.hora = fechaHora.time()
        self.dia = fechaHora.date()

    def crear(self):
        contenido = f""