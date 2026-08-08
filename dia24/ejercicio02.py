def ingresar_sueldo():

    try:
        sueldo = float(input("Ingrese sueldo: "))
        return sueldo

    except ValueError:
        return"Debe ingresar un numero valido"

print(ingresar_sueldo())