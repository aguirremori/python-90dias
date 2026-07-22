try:
    edad = int(input("Ingrese su edad: "))

    if edad <0:
        print("La edad no puede ser negativa")

    elif edad ==0:
        print("La edad debe ser mayor que cero")

    elif edad > 110:
        print("Edad fuera de rango")

    else: 
        print("Edad registrada correctamente")      

except:
    print("Error: Debe ingresar un numero entero.")
