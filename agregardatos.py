def agregar_datos_archivo():
    try:
        archivo = open('datos.cvs', 'a')
        archivo.write('\nLínea 6 agregada')
        archivo.close()
    except FileNotFoundError:
        print('No se encuentra el archivo datos.cvs')
    except Exception as error:
        print('Se ha generado un error no previsto',
type(error).__name__)
agregar_datos_archivo()