#usuarios = {'001':'Marca','002':'Mónica','003':'Jacob'}
#id_usuario = '004'
#añadir = 'La clave 004 no está en el diccionario. Añadiendo clave...'
#
#try:
#    print(usuarios[id_usuario])
#except KeyError: 
#    print(añadir)
#usuarios[id_usuario]= None
#
#print(usuarios)

def error(a,b,c): #se crea funcion error
    try:    #de aca invocamos try
        print(a[b])
    except: #se añade el mensaje de error
        print(c)
    a[b]= None

usuarios = {'001':'Marca','002':'Mónica','003':'Jacob'}
id_usuario = '004'
mensaje = 'La clave 004 no está en el diccionario. Añadiendo clave...'


error(usuarios,id_usuario,mensaje)

print(usuarios)

