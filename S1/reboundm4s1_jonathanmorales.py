class Animal: ##SE  CREA UNA CLASE LLAMADA ANIMAL
    
    def __init__(self,Nombre,Raza,Edad,Peso): 
        self.Nombre = Nombre
        self.Raza = Raza
        self.Edad = Edad
        self.peso = Peso
        
        ##SE AGREGAN FUNCIONES REQUERIDAS
    def comer(self):
        print(f"{self.Nombre} se va alimentar.")
    
    def caminar(self):
        print(f"{self.Nombre} debe caminar para buscar su alimento.")
        
    def dormir(self):
        print(f"Para poder estar activo, {self.Nombre} debe dormir una buena cantidad de horas.")

#AÑADIENDO CARACTERISTICAS 
perro = Animal("Brando","San Bernardo",3,30)
gato = Animal("Roll","Persa",4,3)


##INVOCANDO FUNCIONES
perro.caminar()
perro.comer()
gato.dormir()