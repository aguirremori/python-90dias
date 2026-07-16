
sueldo = int(input("Ingrese el sueldo del trabajador : S/"))

if sueldo < 0:
    print("Error: Sueldo no puede ser negativo, ingresar nuevamente")

elif sueldo < 1025:
    print("Advertencia: El sueldo esta por debajo del sueldo minimo.")

elif sueldo < 10000:
    print("Sueldo valido")

else:
    print("Sueldo alto")