from persona import Persona
from trabajador import Trabajador
from departamento import Departamento

trabajador = Trabajador("Juan","Perez",2005,"Ingenieria de software","IS",20000)


print(trabajador.__dict__)
print("Es Trabajador instancia de Persona?:",(isinstance(trabajador,Persona)))
print("Es trabajor instancia de Departamento?:",(isinstance(trabajador,Departamento)))
print("Es trabajador instancia de Trabajador?:",(isinstance(trabajador,Trabajador)))