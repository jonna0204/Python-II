def remplazar_datos_archivo(texto_viejo, texto_nuevo):
    try:
        archivo = open('datos.cvs', 'r')
        remplazo = ""
        for linea in archivo:
            linea = linea.strip()
            cambios = linea.replace(texto_viejo, texto_nuevo)
            remplazo = remplazo + cambios + "\n"
        archivo.close()
        archivo_remplazo = open('datos.cvs', 'w')
        archivo_remplazo.write(remplazo)
        archivo_remplazo.close()
    except FileNotFoundError:
        print('No se encuentra el archivo datos.cvs')
    except Exception as error:
        print('Se ha generado un error no previsto',type(error).__name__)
    finally:
        print("Se ha remplazado satisfactoriamente")
remplazar_datos_archivo("línea", "LINEA")