class Estadio():
    def __init__(self, nombre, ubicacion, id, capacidad, restaurante):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.id = id
        self.capacidad = capacidad
        self.restaurante = restaurante
        
    def mostrar_estadios(self):
        print(f"Nombre: {self.nombre}\nUbicación: {self.ubicacion}\n")