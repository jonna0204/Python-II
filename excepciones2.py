def division_entera(x,y):
    try:
        dividendo = int(x)
        divisor = int(y)
        return dividendo/divisor
    except ZeroDivisionError:
        print("El divisor no puede ser cero.")
    except Exception as error:
        print("Se ha generado un error no previsto.",type(error.__name__))

resultado = division_entera(1,'q')
print(resultado)