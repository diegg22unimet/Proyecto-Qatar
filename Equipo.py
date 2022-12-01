class Equipo():
    def __init__(self, nombre, codigo, grupo, bandera, id):
        self.nombre = nombre
        self.codigo = codigo
        self.grupo = grupo
        self.bandera = bandera
        self.id = id
        
    def mostrar_equipos(self):
        print(f"Nombre: {self.nombre}\nCódigo: {self.codigo}\nGrupo: {self.grupo}\n")