from herenciaPersona import Persona,Supervisor,Cliente,SupervisorZona


persona1 = Persona("Juan","Perez",123456)
persona2 = Persona("Jose","Sanchez",56789)

supervisor1 = Supervisor("Ariel","Martinez",33434,"Sur")
supervisor2 = Supervisor("Julieta","Morales",2345424,"Norte")

supervisorzona1 = SupervisorZona("Juan","Perez",123455,"Sur",8,25,123)

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
print("******")
print("******")


supervisorzona1.imprimir_datos()
print("******")
supervisorzona1.imprimir_supervisor()
print("******")
supervisorzona1.imprimir_supervisor_zona()



print("******")
print("******")
print("******")
print("******")



print("supervisorzona1")
# Es instancia supervisorzona1 de Persona
print(isinstance(supervisorzona1, Persona))
# Es instancia supervisorzona1 de Supervisor
print(isinstance(supervisorzona1, Supervisor))
# Es instancia supervisorzona1 de SupervisorZona
print(isinstance(supervisorzona1, SupervisorZona))
print("supervisor")
# Es instancia supervisor de Persona
print(isinstance(supervisor1, Persona))
# Es instancia supervisor de Supervisor
print(isinstance(supervisor1, Supervisor))
# Es instancia supervisor de SupervisorZona
print(isinstance(supervisor1, SupervisorZona))
print("******")
print("******")
print("******")
print("******")
print(SupervisorZona.__mro__)
print(Supervisor.__mro__)
print(Persona.__mro__)