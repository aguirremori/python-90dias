while True:
    print("=========MENU==========")
    print("1. Registrar empleado")
    print("2. Buscar empleado")
    print("3. Salir")

    option = int(input("Seleccione una opcion: "))

    if option ==1:
        print("Registrando empleado....")
    elif option ==2:
        print("Buscando empleado....")
    elif option ==3:
        print("Hasta luego")
        break
    else:
        print("Opcion invalida")