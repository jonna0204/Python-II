suma = 3000
contador = 0

try:
    resultado = suma / contador
    print(resultado)
except ZeroDivisionError:
    print("Division por cero.")