class Producto():
    def __init__(self, nombre, cantidad, precio, clasificacion, adicional):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.clasificacion = clasificacion
        self.adicional = adicional
        
    def mostrar_productos(self):
        print(f"Nombre: {self.nombre}\nClasificación: {self.clasificacion}\nAdicional: {self.adicional}\nPrecio: ${(self.precio * 0.16) + self.precio}\n")