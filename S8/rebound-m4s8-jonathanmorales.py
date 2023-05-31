from io import open

def crear_archivo():
    try:
        archivo = open("informacion.dat","x") 
        archivo.close() 
    except FileExistsError:
        print("El archivo informacion.dat existe o a sido creado previamente")
    except Exception as error:
        print("Se ha generado un error no previsto",type(error).__name__) 


def escribir_archivo():
    try:
        with open("informacion.dat","w") as texto:
            texto.write("Datos de información en la línea 1\nDatos de información en la línea 2\nDatos de información en la línea 3\nDatos de información en la línea 4\nDatos de información en la línea 5")
    except FileNotFoundError:
        print("No se encuentra el archivo.")



crear_archivo()
escribir_archivo()