from herenciaPersona import Persona
from herenciaPersona import Supervisor
from herenciaPersona import Cliente

persona1 = Persona("Juan","Perez",123456)
persona2 = Persona("Jose","Sanchez",56789)

supervisor1 = Supervisor("Ariel","Martinez",33434,"Sur")
supervisor2 = Supervisor("Julieta","Morales",2345424,"Norte")

cliente1 = Cliente("Catalina","Lopez",18443234,50)

persona1.imprimir_datos()
persona1.get_tipo()
print("******")
#print(persona1)
persona2.imprimir_datos()
persona2.get_tipo()
#print(persona2)
print("******")
supervisor1.imprimir_supervisor()
supervisor1.get_tipo()
print("******")
supervisor2.imprimir_supervisor()
supervisor2.get_tipo()
print("******")
cliente1.imprimir_cliente()
cliente1.get_tipo()
