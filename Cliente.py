class Cliente():
    def __init__(self, nombre, cedula, edad, id_partido, tipo_entrada, asiento, total_a_pagar):
        self.nombre = nombre 
        self.cedula = cedula
        self.edad = edad
        self.partido = id_partido
        self.entrada = tipo_entrada
        self.asiento = asiento
        self.total_a_pagar = total_a_pagar
    
    def mostrar_clientes(self):
        print(f"{self.nombre}\n{self.cedula}\n{self.edad}\n{self.partido}\n{self.entrada}\n{self.asiento}\n{self.total_a_pagar}")