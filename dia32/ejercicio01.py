numero_valido = False

while numero_valido == False:
    try:
        numero = int(input("Ingrese un numero entero: "))
        print("Numero Ingresado: ",numero)
        numero_valido = True

    except ValueError:
        print("Error: debe ingresar un numero entero")