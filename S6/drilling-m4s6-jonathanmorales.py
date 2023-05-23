
def error(a,b):
    c = f'La clave {b} no está en el diccionario. Añadiendo clave...'
    try:
        print(a[b])
    except KeyError:
        print(c)
    
    a[b] = None

usuarios = {'001','Marca','002','Monica','003','Jacob'}
id_usuario = '004'

error(usuarios,id_usuario)

print(usuarios)