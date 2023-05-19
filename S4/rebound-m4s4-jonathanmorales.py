#Se crea clase libro junto a sus caracteristicas
class Libro: 
    def __init__(self,autor:int=None,titulo:str=None,año:int=None):
        self.autor = autor
        self.titulo = titulo
        self.año = año
    
    #Se crea una funcion imprimir para diferenciar impresion con __dict
    def imprimir(self):
        print(f"autor: {self.autor}, titulo: {self.titulo}, año: {self.año}")
        




libro_1 = Libro("Dan Brown","Inferno")
libro_2 = Libro("Dan Brown","The Da Vinci Code",2003)



print("**********************************")
print(libro_1.__dict__)
libro_1.imprimir()
print("**********************************")
print(libro_2.__dict__)
libro_2.imprimir()
print("**********************************")
