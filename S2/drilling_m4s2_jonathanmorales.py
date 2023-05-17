

#SE CREA LA CLASE PERSONA CON SUS CARACTERISTICAS CORRESPONDIENTES
#SE AGREGAN TIPOS DE DATOS X CARACTERISTICAS
class Persona:
    def __init__(self,nombre:str,apellido:str,sexo:str,edad:int,estatura:float,peso:float):
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.edad = edad
        self.estatura = estatura
        self.peso = peso

    #SE DEFINE FUNCION GET PARA ACCEDER A LOS DATOS
    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def get_sexo(self):
        return self.sexo

    def get_edad(self):
        return self.edad
    
    def get_estatura(self):
        return self.estatura
    
    def get_peso(self):
        return self.peso

    #SE DEFINE FUNCION SET
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_apellido(self, apellido):
        self.apellido = apellido

    def set_sexo(self, sexo):
        self.edad = sexo
        
    def set_edad(self, edad):
        self.edad = edad

    def set_estatura(self, estatura):
        self.estatura = estatura
    
    def set_peso(self, peso):
        self.peso = peso



persona_1 = Persona("Pedro","Vivas","Masculino",20,1.78,68.0)
persona_2 = Persona("Juan","Camargo","Masculino",18,1.80,75.0)

#SE IMPRIME PERSONA1 SIN MODIFICAR
print("----------------------------------")
print(f"{persona_1.get_nombre()} sin modificar su edad:")
print(persona_1.get_edad())
print("----------------------------------")

#SE IMPRIME PERSONA1 MODIFICADA
print(f"{persona_1.get_nombre()} con su edad modificada:")
persona_1.set_edad(21)
print(persona_1.get_edad())
print("----------------------------------")

#SE IMPRIME PERSONA2 SIN MODIFICAR
print(f"{persona_2.get_nombre()} sin modificar su apellido:")
print(persona_2.get_nombre(), persona_2.get_apellido())
print("----------------------------------")

#SE IMPRIME PERSONA2 MODIFICADA
print(f"{persona_2.get_nombre()} con su apellido modificado:")
persona_2.set_apellido("Santiago")
print(persona_2.get_nombre(), persona_2.get_apellido())
print("----------------------------------")




