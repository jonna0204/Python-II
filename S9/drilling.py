import time

def crear_archivo():
    try:
        archivo = open("informacion.dat","x",encoding="utf-8") 
        archivo.close() 
    except FileExistsError:
        print("El archivo informacion.dat existe o a sido creado previamente")
    except Exception as error:
        print("Se ha generado un error no previsto",type(error).__name__) 

def escribir_archivo(texto):
    try:
        with open("informacion.dat","r") as existente:
            contenido_existente = existente.read()
        
        with open("informacion.dat", "a") as archivo:
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

def remplazar_datos_archivo(texto_viejo, texto_nuevo):
    try:
        archivo = open('informacion.dat', 'r')  #  aperturar archivo
        lineas = archivo.readlines()  #  leer lineas
        archivo.close()  #  cerrar archivo

        remplazo = ""  #  acumular las lineas reemplazadas
        contador = 0  #  contador de lineas reemplazadas

        for linea in lineas:  #  se recorre la lista de lineas
            if texto_viejo in linea:  #  se verifica si el texto_viejo existe en la linea que se recorre
                linea = linea.replace(texto_viejo, texto_nuevo)  #  se reemplaza el texto_viejo con el texto_nuevo
                contador += 1  #  se cuenta el reemplazo
            remplazo += linea  # se acumula la linea

        if contador > 0:  #  se verifica el contador si se reemplazaron lineas 
            archivo_remplazo = open('informacion.dat', 'w', encoding='utf-8')
            archivo_remplazo.write(remplazo)  #  se escribe en el archivo
            archivo_remplazo.close()  #  se cierra el archivo

        print("Se realizaron {} remplazos".format(contador))

    except FileNotFoundError:
        print('No se encuentra el archivo informacion.dat')
    except Exception as error:
        print('Se ha generado un error no previsto:', type(error).__name__)





crear_archivo()
escribir_archivo("Hola mundo\nEste es una nueva línea en el archivo\nagregando la segunda línea del archivo\nfinalizando la línea agregada\n")
escribir_archivo("Datos de información en la línea 5\n")
escribir_archivo("Datos de información en la línea 4\n")
escribir_archivo("Datos de información en la línea 3\n")
escribir_archivo("Datos de información en la línea 2\n")
escribir_archivo("Datos de información en la línea 1\n")

remplazar_datos_archivo("información", "Procesamiento")

