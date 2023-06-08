import time

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
    #print(str(automovil_creado))

print("Imprimiendo por pantalla los Vehiculos:")
imprimir_datos(lista)


#print(lista)