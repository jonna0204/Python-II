###Se define la clase definida x el usuario
class alerta(Exception):
    def __init__(self,salario,mensaje="Salario no esta definido en el rango de (1000 a 2000)."):
        self.mensaje = mensaje
        self.salario = salario
        super().__init__(self.mensaje)
        
        

###se define la funcion a utilizar
def excepcion():
    while True:
        salario = int(input("ingresa tu salario: "))##cliente agrega el salario
        if not 1000 <= salario <= 2000:
            raise alerta(salario)   #si el salario esta fuera del rango se llama a la clase creada
        else:
            print(f"Tu salario es valido de {salario} y esta dentro del rango valido.")#Si el salario el valido se imprime
            break

excepcion() #se llama a la funcion
