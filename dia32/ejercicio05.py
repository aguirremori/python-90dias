try:
    numero = int(input("Ingrese un numero: "))

except ValueError:
    print("Error: Debe ingresar un numero entero")

else:
    if numero >= 1 and numero <= 100:
        print("Numero valido")
    else:
        print("Numero fuera de rango")