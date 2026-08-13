empleado = {
    "codigo": "E001",
    "nombre": "Juan Perez",
    "rol": "Supervisor",
    "sueldo": 3500
}
def calcular_sueldo_anual(sueldo):
    return sueldo*12

def calcular_bono(sueldo_anual,porcentaje):
    return sueldo_anual*porcentaje*1/100

sueldo_anual = calcular_sueldo_anual(empleado["sueldo"])
bono = calcular_bono(sueldo_anual,10)

print("Empleado: ",empleado["nombre"])
print("Sueldo_anual: S/",sueldo_anual)
print("Bono: S/", bono)