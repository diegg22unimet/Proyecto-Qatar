class Partido():
    def __init__(self, local, visitante, fecha_hora, estadio, id):
        self.local = local
        self.visitante = visitante
        self.fecha = fecha_hora
        self.estadio = estadio
        self.id = id
        
    def mostrar_partidos(self):
        print(f"ID Partido: {self.id}\nEquipo local: {self.local}\nEquipo visitante: {self.visitante}\nFecha: {self.fecha}\nEstadio: {self.estadio}\n")