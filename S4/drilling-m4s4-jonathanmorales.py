#Se crea clase persona junto a su unica caracteristica
class Persona:
    def __init__(self,nombre) -> None:
        self.nombre = nombre

    #Funcion para el movimiento solicitado
    def movimiento(self,estado):
        print(f"{self.nombre} en estos momentos se encuentra {estado}.")

#Se crea subclase dentro de la clase Persona
class Maratonista(Persona):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)
    
    def movimiento(self,estado):
        print(f"{self.nombre} en estos momentos se encuentra {estado}.")

#Se crea subclase dentro de la clase Persona
class Ciclista(Persona):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)
    
    def movimiento(self,estado):
        print(f"{self.nombre} en estos momentos se encuentra {estado}.")

#Se añaden nombres a la clase y subclase
persona_1 = Persona('Jonathan')
ciclista = Ciclista('Julieta')
maratonista = Maratonista('Catalina')

#Se imprime estado de movimiento de la clase y subclases
persona_1.movimiento('Caminando')
ciclista.movimiento('rodando')
maratonista.movimiento('trotando')