numero_valido = False

while not numero_valido:
    try:
        numero = int(input("Ingrese un numero entero: "))
        print("Numero Ingresado: ",numero)
        numero_valido = True

    except ValueError:
        print("Error: debe ingresar un numero entero")