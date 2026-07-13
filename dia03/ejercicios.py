nombre = input("Nombre del empleado: ")

sueldo = float(input("Sueldo base: "))
bono = float(input("Bono: "))
horas_extras = float(input("Horas extras: "))

afp = float(input("AFP: "))
quinta = float(input("Quinta: "))

sueldo_bruto = sueldo + bono + horas_extras
descuentos_totales = afp + quinta
sueldo_neto = sueldo_bruto - afp - quinta

print()
print("======== PLANILLA===========")
print("Empleado:", nombre)
print("AFP: S/", afp)
print("Quinta Categoria: S/", quinta)
print()
print("Sueldo Bruto: S/", sueldo_bruto)
print("Descuentos Totales: -S/", descuentos_totales)
print("------------------------------")
print("Sueldo Neto: S/",sueldo_neto)
