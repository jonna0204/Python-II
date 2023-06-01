def eliminar_datos_archivo():
    try:
        archivo = open('datos.cvs', 'w')
        archivo.close()
    except FileNotFoundError:
        print('No se encuentra el archivo datos.cvs')
    except Exception as error:
        print('Se ha generado un error no previsto',type(error).__name__)
    finally:
        print("Se ha eliminado todos los datos del archivo exitosamente")
eliminar_datos_archivo()