import calculos

empleado = {
    "codigo": "E001",
    "nombre": "Juan Perez",
    "rol": "Supervisor",
    "sueldo": 3500
}
sueldo = empleado["sueldo"]

sueldo_anual = calculos.calcular_sueldo_anual(sueldo)
porcentaje,bono = calculos.calcular_bono(sueldo_anual)

print("Nombre: ",empleado["nombre"])
print("Sueldo mensual: S/",empleado["sueldo"])
print("Sueldo anual: S/",sueldo_anual)
print("Porcentaje de bono: ",porcentaje)
print("Monto del bono: S/", bono)