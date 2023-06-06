import time

def crear_archivo():
    try:
        archivo = open("informacion.dat","x") 
        archivo.close() 
    except FileExistsError:
        print("El archivo informacion.dat existe o a sido creado previamente")
    except Exception as error:
        print("Se ha generado un error no previsto",type(error).__name__) 

def escribir_archivo(texto):
    try:
        with open("informacion.dat","r") as existente:
            contenido_existente = existente.read()
        
        with open("informacion.dat", "w") as archivo:
            nuevo = archivo.write(texto + contenido_existente)
    except FileNotFoundError:
        print("No se encuentra el archivo.")
    except Exception as e:
        print("ERROR: ", e)

def lectura_archivo():
    try:
        archivo = open("informacion.dat", "r")
        contenido = archivo.read()
        archivo.close()
        print(contenido)
    except FileNotFoundError:
        print("No se encuentra el archivo informacion.dat")
    except Exception as error:
        print("Se ha generado un error no previsto",type(error).__name__) 


crear_archivo()
escribir_archivo("Hola mundo\nEste es una nueva línea en el archivo\nagregando la segunda línea del archivo\nfinalizando la línea agregada")
print("*****************************************************************")



escribir_archivo("Datos de información en la línea 5\n")
escribir_archivo("Datos de información en la línea 4\n")
escribir_archivo("Datos de información en la línea 3\n")
escribir_archivo("Datos de información en la línea 2\n")
escribir_archivo("Datos de información en la línea 1\n")
time.sleep(2)
lectura_archivo()

