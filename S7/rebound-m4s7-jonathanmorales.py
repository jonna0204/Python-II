while True:
    print("Ingresa tu edad: ")
    edad = int((input()))
    print(f"Tu tienes {edad} años.")
    
    try:
        if edad >= 18:
            print("Eres mayor de edad")
            break
        elif edad < 18: 
            print("Eres menor de edad")
            break
    except ValueError:
        print("La entrada no es un número válido")






