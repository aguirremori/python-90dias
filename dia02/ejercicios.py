nombre = "Carlos Perez"

sueldo = 4500
bono = 300
horas_extras = 250
descuento_afp = 520
descuento_quinta = 180

sueldo_bruto = sueldo + bono + horas_extras
sueldo_neto = sueldo_bruto - descuento_afp -descuento_quinta

print("============ PLANILLA =============")
print()
print("Empleado:",nombre)
print("Sueldo Base: S/", sueldo)
print("Bono: S/",bono)
print("Horas Extras: S/",horas_extras)
print("-----------------------------------")
print("Sueldo Bruto: S/",sueldo_bruto)
print("-----------------------------------")
print("Descuento AFP: -S/",descuento_afp)
print("Descuento Quinta: -S/",descuento_quinta)
print("-----------------------------------")
print("Sueldo Neto: S/",sueldo_neto)

