import time
import csv

class Vehiculo:
    def __init__(self, marca, modelo, nruedas):
        self.marca = marca
        self.modelo = modelo
        self.nruedas = nruedas

    def __str__(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}, Ruedas: {self.nruedas}'

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, nruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, nruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f'{super().__str__()}, Velocidad: {self.velocidad} Km/h, Cilindrada: {self.cilindrada} cc.'

class Particular(Automovil):
    def __init__(self, marca, modelo, nruedas, velocidad, cilindrada, numero_puestos):
        super().__init__(marca, modelo, nruedas, velocidad, cilindrada)
        self.numero_puestos = numero_puestos
    
    def __str__(self):
        return f'{super().__str__()}, Numeros puestos: {self.numero_puestos}'

class Carga(Automovil):
    def __init__(self, marca, modelo, nruedas, velocidad, cilindrada, peso_carga):
        super().__init__(marca, modelo, nruedas, velocidad, cilindrada)
        self.peso_carga = peso_carga
    
    def __str__(self):
        return f'{super().__str__()}, Peso de carga: {self.peso_carga}'

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, nruedas, tipo):
        super().__init__(marca, modelo, nruedas)
        self.tipo = tipo
    
    def __str__(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}, Ruedas: {self.nruedas}, Tipo: {self.tipo}'

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, nruedas, tipo, numero_radios, cuadro, motor):
        super().__init__(marca, modelo, nruedas, tipo)
        self.numero_radios = numero_radios
        self.cuadro = cuadro
        self.motor = motor

    def __str__(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}, Ruedas: {self.nruedas}, Tipo: {self.tipo}, Numero de radios: {self.numero_radios}, Cuadro: {self.cuadro}, Motor: {self.motor}'

"""
def agregar_datos():
    time.sleep(1)
    marca = input("Inserte la marca del automóvil: ")
    modelo = input("Inserte el modelo: ")
    numero_ruedas = int(input("Inserte el número de ruedas: "))
    velocidad = int(input("Inserte la velocidad: "))
    cilindrada = int(input("Inserte la cilindrada: "))
    print("**********************************************************")

    return Automovil(marca, modelo, numero_ruedas, velocidad, cilindrada)  

def imprimir_datos(lista):
    for i, automovil in enumerate(lista, 1):
        print(f"Datos del automóvil {i} : Marca {automovil.marca}, Modelo {automovil.modelo}, {automovil.nruedas} ,ruedas {automovil.velocidad} Km/h, {automovil.cilindrada} cc")
"""


def crear_archivo():
    try:
        archivo = open("vehiculo.csv", "x") 
        archivo.close() 
    except FileExistsError:
        print("El archivo vehiculo.csv existe o ha sido creado previamente")
    except Exception as error:
        print("Se ha generado un error no previsto", type(error).__name__) 

def leer_datos_csv(nombre_archivo):
    try:
        vehiculos = []
        vehiculos.append({"Lista de Vehiculos Particular:": (particular.__dict__)})
        vehiculos.append({"Lista de Vehiculos Carga:": (carga.__dict__)})
        vehiculos.append({"Lista de Vehiculos Bicicleta:": (bicicleta.__dict__)})
        vehiculos.append({"Lista de Vehiculos Motocicleta:": (motocicleta.__dict__)})
        with open(nombre_archivo, "r") as archivo:
            for vehiculo in vehiculos:
                for i, j in vehiculo.items():
                    print(i)
                    print(j)
    except FileNotFoundError:
        print('No se encuentra el archivo vehiculo.csv')
    except Exception as error:
        print('Se ha generado un error no previsto:', type(error).__name__)

"""
print("**********************************************************")
ingreso = int(input('Ingrese cuantos vehiculos se crearan: '))
print("**********************************************************")
lista = [] #lista vacia
agregar_datos()
for i in range(1,ingreso+1):
    automovil_creado = agregar_datos()
    lista.append(automovil_creado)
    time.sleep(1)
    print(f'Se ha creado el automovil numero {i}')
    print("**********************************************************")


print("Imprimiendo por pantalla los Vehiculos:")
imprimir_datos(lista)
"""

"""
print(particular.__dict__)
print(carga.__dict__)
print(bicicleta.__dict__)
print(motocicleta.__dict__)

print("Motocicleta es instancia con relación a Vehículo:", isinstance(motocicleta, Vehiculo))
print("Motocicleta es instancia con relación a Automovil:", isinstance(motocicleta, Automovil))
print("Motocicleta es instancia con relación a Vehículo particular:", isinstance(motocicleta, Particular))
print("Motocicleta es instancia con relación a Vehículo de Carga:", isinstance(motocicleta, Carga))
print("Motocicleta es instancia con relación a Bicicleta:", isinstance(motocicleta, Bicicleta))
print("Motocicleta es instancia con relación a Motocicleta:", isinstance(motocicleta, Motocicleta))
"""


crear_archivo()

particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)



leer_datos_csv("vehiculo.csv")