empleado = {
    "codigo": "E001",
    "nombre": "Juan Perez",
    "rol": "Supervisor",
    "sueldo": 3500
}

def calcular_sueldo_anual(sueldo):
    return sueldo*12

sueldo = empleado["sueldo"]
sueldo_anual = calcular_sueldo_anual(sueldo)

print("Empleado: ", empleado["nombre"])
print("Sueldo mensual: S/", sueldo)
print("Sueldo anual: S/",sueldo_anual)