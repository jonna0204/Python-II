class Vehiculo:
    #constructor con parametros para realizar una instancia de la clase Vehiculo
    def __init__(self, marca, modelo, nruedas):
        self.marca = marca
        self.modelo = modelo
        self.nruedas = nruedas

class Automovil(Vehiculo): #SE CREA CLASE SUPERVISOR HEREDANDO SIMPLE DE CLASE PERSONA
    def __init__(self,marca,modelo,nruedas, velocidad,cilindrada):
        super().__init__(marca,modelo,nruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def __str__(self):
        return f'Marca:{self.marca},Modelo:{self.modelo},Ruedas:{self.nruedas},Velocidad:{self.velocidad},Cilindrada:{self.cilindrada}'

def agregar_datos():
    marca = input("Inserte la marca del automovil: ")
    modelo = input("Inserte el modelo: ")
    numero_ruedas = input("Inserte el número de ruedas: ")
    velocidad = input("Inserte la velocidad: ")
    cilindrada = input("Inserte la cilindrada: ")


def imprimir_datos():
    
    for i in range(1,cantidad+1):
        creado = agregar_datos()
        lista.append(creado)
        print(f"Hemos creado el automovil numero: {i}")
        
        

lista = []
cantidad = int(input("Cuantos vehiculos deseas insertar: "))
agregar_datos()
imprimir_datos()