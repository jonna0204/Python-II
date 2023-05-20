class Persona: ##SE CREA CLASE PERSONA CON SUS CARACTERISTICAS
    def __init__(self, nombre, apellidos, cedula):
        self.nombre = nombre
        self.apellidos = apellidos
        self.cedula = cedula
    
    def imprimir_datos(self): #SE CREA FUNCION QUE IMPRIME LOS DATOS
        print(f"Nombre: {self.nombre} \nApellidos: {self.apellidos} \nCedula: {self.cedula}")
    
    def get_tipo(self):
        print("Soy del tipo Persona.")
    
    def __str__(self): #FUNCION PARA ACCEDER A LOS DATOS DE FORMA STRING
        return f"Nombre: {self.nombre} \nApellidos: {self.apellidos}\nCedula: {self.cedula}"
    


class Supervisor(Persona): #SE CREA CLASE SUPERVISOR HEREDANDO SIMPLE DE CLASE PERSONA
    def __init__(self, nombre, apellidos, cedula, zona):
        super().__init__(nombre, apellidos, cedula) 
        self.zona = zona
    
    def imprimir_supervisor(self):
        super().imprimir_datos()
        print("Zona: ",self.zona)
    
    def get_tipo(self):
        print("Soy del tipo Supervisor.")
    
    def __str__(self):
        return super().__str__() + f"\nZona: {self.zona}"

class Cliente(Persona):
    def __init__(self, nombre, apellidos, cedula, descuento ):
        super().__init__(nombre, apellidos, cedula)
        self.descuento = descuento

    def imprimir_cliente(self):
        super().imprimir_datos()
        print('Descuento: ', self.descuento)
    
    def get_tipo(self):
        print("Soy del tipo Cliente.")
    
    def __str__(self):
        return super().__str__() + f'\nDescuento: {self.descuento}'

class Capacidades:
    def __init__(self,ncertificados,raiting):
        self.ncertificados = ncertificados
        self.raiting = raiting
    
    def imprimir_capacidades(self):
        print(f"Nro. Certificados: {self.ncertificados} \nRaiting: {self.raiting}")
    
    def __str__(self):
        return f"Numero de certificados: {self.ncertificados} \nRaiting: {self.raiting}"

class SupervisorZona(Supervisor,Capacidades):
    def __init__(self, nombre, apellidos, cedula, zona,ncertificados,raiting,promedio):
        Supervisor.__init__(self,nombre,apellidos,cedula,zona)
        Capacidades.__init__(self,ncertificados,raiting)
        self.promedio = promedio
    
    def imprimir_supervisor_zona(self):
        Supervisor.imprimir_supervisor(self)
        Capacidades.imprimir_capacidades(self)
        print("Promedio",self.promedio)