from persona import Persona
from departamento import Departamento

class Trabajador(Persona,Departamento):
    def __init__(self, nombre, apellido, anno,nombre_dpto,nombre_corto_dpto,salario):
        Persona.__init__(self,nombre,apellido,anno)
        Departamento.__init__(self,nombre_dpto,nombre_corto_dpto)
        self.salario = salario
    

