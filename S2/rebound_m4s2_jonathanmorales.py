class Animal:
    def __init__(self,nombre,raza,edad,peso):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
    
    def nombre_(self):
        return self.nombre
    
    def raza_(self):
        return self.raza
    
    def edad_(self):
        return self.edad
    
    def peso_(self):
        return self.peso
    

caballo = Animal("Zeus","Pura sangre",5,450)
leon = Animal("Boulder","Atlas",10,130)

print(caballo.nombre_())
print(leon.peso_())

caballo.nombre_()






