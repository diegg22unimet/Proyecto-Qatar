import pip._vendor.requests
import itertools as it
import random
from Equipo import Equipo
from Estadio import Estadio
from Partido import Partido
from Cliente import Cliente
from Producto import Producto

#Listas para almacenar los datos de las API's y otros datos
lista_equipos = []
lista_estadios = []
lista_partidos = []
lista_fechas = []
lista_clientes = []
lista_restaurantes =[]
lista_productos = []
nombre_p = []
tipo_p = []

#----------------------------------------------------------------------------------------------------------------------
# MÓDULO 1
#----------------------------------------------------------------------------------------------------------------------

#Manejo de la clase Equipo
def registrar_equipos():
    url1 = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/teams.json"
    data1 = pip._vendor.requests.get(url1)
    if data1.status_code == 200:
        data1 = data1.json()
    for i in data1:
        equipo = Equipo(i["name"], i["fifa_code"], i["group"], i["flag"], i["id"])
        lista_equipos.append(equipo)
        
def ver_equipos():
    for i in lista_equipos:
        i.mostrar_equipos()
        
        
#Manejo de la clase Estadio
def registrar_estadios():
    url2 = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/stadiums.json"
    data2 = pip._vendor.requests.get(url2)
    if data2.status_code == 200:
        data2 = data2.json()
    for i in data2:
        estadio = Estadio(i["name"], i["location"], i["id"], i["capacity"], i["restaurants"])
        lista_estadios.append(estadio)
    
def ver_estadios():
    for i in lista_estadios:
        i.mostrar_estadios()
        
        
#Manejo de la clase Partido
def registrar_partidos():
    url3 = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/matches.json"
    data3 = pip._vendor.requests.get(url3)
    if data3.status_code == 200:
        data3 = data3.json()
    for i in data3:
        for y in lista_equipos:
            if i["home_team"] == y.nombre:                  #Realizando la importación de datos para la referencia al objeto
                local = y.nombre
        for y in lista_equipos:
            if i["away_team"] == y.nombre:
                visitante = y.nombre
        partido = Partido(local, visitante, i["date"], i["stadium_id"], i["id"])
        lista_partidos.append(partido)
    for y in lista_estadios:
        for x in lista_partidos:
            if y.id == x.estadio:
                x.estadio = y.nombre
    for j in lista_partidos:                               #Éstas líneas de código permiten separan la fecha y la hora de la API de partido
        if " " in j.fecha:
            if j.fecha.split(" ")[0] not in lista_fechas:
                lista_fechas.append(j.fecha.split(" ")[0]) 
                
def ver_partidos():
    for i in lista_partidos:
        i.mostrar_partidos()
        
# FIN MÓDULO 1
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



#----------------------------------------------------------------------------------------------------------------------
# MÓDULO 2
#----------------------------------------------------------------------------------------------------------------------

#Manejo de la clase Cliente
def registrar_clientes():
    compra_realizada = False
    
    id_partido = input("De acuerdo a la lista de partidos mostrada anteriormente, indique el ID del partido al cual desea asistir:  ")
    while not id_partido.isnumeric() or int(id_partido) not in range(1,49):
        id_partido = input("Introduzca un número de ID válido:  ")
    
    tipo_entrada = input("Elige el tipo de entrada que deseas:\n1. General\n2. VIP\n--> ")
    while not tipo_entrada.isnumeric() or int(tipo_entrada) not in range(1,3):
        tipo_entrada = input("Elige un tipo de entrada válida:\n1. General\n2. VIP\n--> ")  
    if tipo_entrada == "1":
        tipo_entrada = "General"
    else:
        tipo_entrada = "VIP"
        
    nombre = input("Ingrese su nombre (Sin espacios): ").title()
    while not nombre.isalpha() or nombre.isspace():
        nombre = input("Ingrese un nombre completo válido: ")
        
    cedula = input("Ingrese un número de cédula (Máx: V-100.000): ")
    while not cedula.isnumeric() or int(cedula) not in range(1, 100001): 
        cedula = input("Ingrese un número de cédula válido: ")
        
    edad = input("Ingrese su edad: ")
    while not edad.isnumeric() or int(edad) == 0:
        edad = input("Ingrese una edad válida: ")

    asiento = random.randrange(1, 40)

    total_a_pagar = factura_entradas(int(cedula), tipo_entrada, vampiros, asiento)
    
    confirmacion = input("¿Desea realizar la compra?\n1. Sí\n2. No\n-> ")
    while not confirmacion.isnumeric() or int(confirmacion) not in range(1,3):
        confirmacion = input("Introduzca una opción válida:\n1. Sí\n2. No\n-> ")
    if confirmacion == "1":
        compra_realizada = True
        cliente = Cliente(nombre, cedula, edad, id_partido, tipo_entrada, asiento, total_a_pagar)
        lista_clientes.append(cliente)
        print("Compra realizada con éxito")
    else:
        print("Compra descartada")
        
    return cedula, tipo_entrada, id_partido, asiento


def ver_clientes():
    for i in lista_clientes:
        i.mostrar_clientes()

#Funciones para crear mostrar el mapa y asientos
'''def crear_mapas(asientos_gen, asientos_vip):
    #Para los mapas de clientes VIP
    asientos = asientos_vip
    columna = asientos // 10
    filas = ['A','B','C','D','E','F','G','H','I','J']
    aux = 1
    for i in range(columna):
        fila1 = []
        aux1 = 0
        for i in range(len(filas)):
            num = filas[aux1] + str(aux)
            aux1 += 1
            fila1.append(num)
        aux += 1
        vip.append(fila1)
        
    #Para los mapas de clientes General
    asientos = asientos_gen
    columna = asientos // 10
    for i in range(columna):
        fila1 = []
        aux1 = 0
        for i in range(len(filas)):
            num = filas[aux1] + str(aux)
            aux1 += 1
            fila1.append(num)
        aux += 1
        generales.append(fila1)
        
        return vip, generales'''
        

'''def mostrar_mapa(tipo_entrada, id_partido):
    if tipo_entrada == "General":
        for i in lista_partidos:
            if i.id == id_partido:
                mapa = i.asientos_gen
                
    if tipo_entrada == "VIP":
        for i in lista_partidos:
            if i.id == id_partido:
                mapa = i.asientos_vip
                
    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            print(mapa[i][j], end = "    ")
        print()
        
    return mapa'''


'''def elegir_asientos(mapa, id_partido, tipo_entrada):
    asiento_ocupado = "S"
    asiento_disponible = "N"
    while not asiento_disponible == asiento_ocupado:
        asiento_disponible = input("Ingrese la silla que desea reservar: ").upper()
        existe = False
        for i in range(len(mapa)):
            for j in range(len(mapa[i])):
                if (mapa[i][j])[:-1] == asiento_disponible and (mapa[i][j])[-1] == "*":
                    print("El asiento que seleccionó está ocupado, seleccione otro asiento: ")
                    existe = True
                    break
                
                elif mapa[i][j] == asiento_disponible:
                    mapa[i][j] += "*"
                    existe = True
                    asiento_ocupado = asiento_disponible
                    break
                
            if existe == True:
                break
            
        if not existe:
            print("Opción inválida, intente de nuevo: ")
    
    for i in lista_partidos:
        if i.id == id_partido:
            if tipo_entrada == "General":
                i.asientos_gen = mapa
            else:
                i.asientos_vip = mapa
                
    return asiento_disponible'''

    
'''def asientos(asientos_gen, asientos_vip):
    asientos = asientos_gen + asientos_vip
    asientos_no_disponibles = []
    columnas = asientos / 10
    filas = ['A','B','C','D','E','F','G','H','I','J']
    aux = 1
    for i in range(columnas):
        fila = []
        aux1 = 0
        for i in range(len(filas)):
            num = filas[aux1] + str(aux)
            aux1 += 1
        asientos_no_disponibles.append(fila) 
        
    return asientos_no_disponibles
'''

#Código para validar si la cédula del cliente es un número vampiro y generar la factura
def factura_entradas(cedula, tipo_entrada, vampiros, asiento):
    total = 0
    descuento = 0
    vampiro = False
    
    if tipo_entrada == "General":
        subtotal = 50
    else:
        subtotal = 120
    
    impuesto =  subtotal * 0.16
    
    for i in vampiros:
        if int(i) == cedula:
            vampiro = True
            break
    
    if vampiro == True:                                         #Si la cédula del cliente resulta nro. vampiro se le muestra un mensaje en pantalla 
        descuento = subtotal * 0.50
        total = subtotal + impuesto - descuento
        print(f"\n¡Felicidades! Su cédula es un número vampiro. Se le ha aplicado un 50% de descuento en el precio de su entrada.\n----- ENTRADA -----\nAsiento: {asiento}\nSubtotal: ${subtotal}\nIVA: ${impuesto}\nDescuento: -${descuento}\nMonto a pagar: ${round(total, 2)}\n")
    else:
        descuento = 0                                           #En cambio, si no lo es, se le genera la factura sin el renglón descuento
        total = subtotal + impuesto - descuento
        print(f"\n----- ENTRADA -----\nAsiento: {asiento}\nSubtotal: ${subtotal}\nIVA: ${impuesto}\nMonto a pagar: ${round(total, 2)}\n")
        
    return total


#Código para obtener los números vampiros que existen desde el 1 hasta el 100.000 
vampiros = []

def get_combinaciones(num_str):
    num_iter = it.permutations(num_str, len(num_str))
    for num_list in num_iter:
        v = ''.join(num_list)
        x, y = v[:int(len(v)/2)], v[int(len(v)/2):]
        if x[-1] == '0' and y[-1] == '0':
            continue
        if int(x) * int(y) == int(num_str):
            return x,y
    return False

def es_vampiro(m_int):
    n_str = str(m_int)
    if len(n_str) % 2 == 1:
        return False
    combinaciones = get_combinaciones(n_str)
    if not combinaciones:
        return False
    return True

for test_num in range(100000):
    if es_vampiro(test_num):
        vampiros.append(test_num)
            
# FIN MÓDULO 2
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



#----------------------------------------------------------------------------------------------------------------------
# MÓDULO 4
#----------------------------------------------------------------------------------------------------------------------

def registrar_productos():
    for i in lista_estadios:
        for j in i.restaurante:
            for x in j["products"]:
                producto = Producto(x["name"], x["quantity"], x["price"], x["type"], x["adicional"])
                lista_productos.append(producto)
    for i in lista_productos:
        if i.nombre not in nombre_p:
            nombre_p.append(i.nombre)
        if i.clasificacion not in tipo_p:
            tipo_p.append(i.clasificacion)
    
def ver_productos():
    for i in lista_productos:
        i.mostrar_productos()     
        
def venta_restaurante():
    permitido = False
    
    cedula = cedula = input("Ingrese un número de cédula (Máx: V-100.000): ")
    while not cedula.isnumeric() or int(cedula) not in range(1, 100001): 
        cedula = input("Ingrese un número de cédula válido: ")
        
    for i in lista_clientes:
        if i.cedula == cedula and i.tipo_entrada == "VIP":
                permitido = True
                print("Cédula validada, disfrute de los servicios de nuestro restaurante")
        else:
            print("Acceso al restaurante denegado")
            break
                
    if permitido == True:
        pedido = input("¿Qué desea comer?")


#Inicializador del proyecto
def main():
    registrar_equipos()
    registrar_estadios()
    registrar_partidos()
    while True:
        o = input("\n        ------- BIENVENIDO AL SITIO OFICIAL DE LA FIFA -------\n\nEsta página esta destinada para que puedas seguir más de cerca tu deporte favorito\n\n1. Buscar partidos\n2. Comprar entradas\n3. Ver asistencia a partidos\n4. Ver productos de restaurantes\n5. Venta de restaurantes\n6. Indicadores de Gestión\n7. Salir del programa\n\nIngrese la opción que desee realizar: ")
        print()
        while not o.isnumeric() or int(o) not in range(1,8):
            o = input("\n1. Buscar partidos\n2. Comprar entradas\n3. Ver asistencia a partidos\n4. Ver productos de restaurantes\n5. Venta de restaurantes\n6. Indicadores de Gestión\n7. Salir del programa\n\nIngrese una opción válida: ")
        
        if o == "1":
            o2 = input("1. Buscar todos los partidos de un equipo\n2. Buscar todos los partidos de un estadio\n3. Buscar todos los partidos de una fecha.\n\nIngrese la opción que desee realizar: ")
            print()
            while not o2.isnumeric() or int(o2) not in range(1,4):
                o2 = input("1. Buscar todos los partidos de un equipo\n2. Buscar todos los partidos de un estadio\n3. Buscar todos los partidos de una fecha.\n\nIngrese una opción válida: ")
            
            #Búsqueda de partidos por equipo
            if o2 == "1":
                j = 0
                for i in lista_equipos:
                    print(f"{j+1}. {i.nombre}")
                    j += 1
                print()
                pais = input("Seleccione el equipo que desee para visualizar todos sus partidos: ")
                while not pais.isnumeric() or int(pais) not in range(1,33):
                    pais = input("Seleccione una opción válida: ")
                print()
                for x in lista_partidos:
                    if x.local == lista_equipos[int(pais)-1].nombre or x.visitante == lista_equipos[int(pais)-1].nombre:
                        x.mostrar_partidos()
                        print()
                print()
                    
            #Busqueda de partidos por estadio
            elif o2 == "2":
                j = 0
                for i in lista_estadios:
                    print(f"{j+1}. {i.nombre}")
                    j += 1
                print()
                estadio = input("Seleccione el estadio que desee para visualizar todos sus partidos: ")
                while not estadio.isnumeric() or int(estadio) not in range(1,9):
                    estadio = input("Seleccione una opción válida: ")
                print()
                for x in lista_partidos:
                    if x.estadio == lista_estadios[int(estadio)-1].nombre:
                        x.mostrar_partidos()
                        print()
                print()
                
            #Busqueda de partido por fecha
            else:
                j = 0
                for i in lista_fechas:
                    print(f"{j+1}. {i}")
                    j += 1
                print()
                dia = input("Seleccione la fecha que desee para visualizar todos sus partidos: ")
                while not dia.isnumeric() or int(dia) not in range(1,14):
                    dia = input("Seleccione una opción válida: ")
                print()
                for x in lista_partidos:
                    if x.fecha.split(" ")[0] == lista_fechas[int(dia)-1]:
                        x.mostrar_partidos()
                        print()
                print()
                
        elif o == "2":
            for i in lista_partidos:
                i.mostrar_partidos()
            registrar_clientes()
            
        elif o == "3":
            print(":(")
            
        elif o == "4":
            registrar_productos()
            o3 = input("1. Buscar todos los productos por nombre\n2. Buscar todos los productos por tipo\n\nIngrese la opción que desee realizar: ")
            print()
            while not o3.isnumeric() or int(o3) not in range(1,3):
                o3 = input("1. Buscar todos los productos por nombre\n2. Buscar todos los productos por tipo\n\nIngrese una opción válida: ")
                
            #Búsqueda de productos por nombre
            if o3 == "1":
                j = 0
                for i in nombre_p:
                    print(f"{j+1}. {i}")
                    j += 1
                print()
                item = input("Seleccione el producto que desee para visualizar sus especificaciones: ")
                while not item.isnumeric() or int(item) not in range(1,9):
                    item = input("Seleccione una opción válida: ")
                print()
                for x in lista_productos:
                    if x.nombre == nombre_p[int(item)-1]:
                        x.mostrar_productos()
                print()
                
            #Búsqueda de productos por su clasificación
            else:
                j = 0
                for i in tipo_p:
                    print(f"{j+1}. {i}")
                    j += 1
                print()
                tipo = input("Seleccione el tipo de producto que desee para visualizar : ")
                while not tipo.isnumeric() or int(tipo) not in range(1,2):
                    tipo = input("Seleccione una opción válida: ")
                print()
                for x in lista_productos:
                    if x.clasificacion == tipo_p[int(tipo)-1]:
                        x.mostrar_productos()
                print()
            
        elif o == "5":
            venta_restaurante()
        
        elif o == "6":
            print(":(")
            
        elif o == "7":
            print("¡Gracias por confiar en nosotros! Le deseamos mucho éxito")
            break
        print()
main()