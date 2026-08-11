try:
    edad = int(input("Ingrese su edad: "))

except ValueError:
    print("Error: Debe ingresar un numero entero")

else:
    if edad >= 1 and edad <= 120:
        print("Edad valida")
    else:
        print("Edad fuera de rango")