empleado1 = {
    "nombre": "Juan Perez",
    "sueldo": 3500
}

empleado2 = {
    "nombre": "Ana Lopez",
    "sueldo": 2800
}
def calcular_sueldo_anual(sueldo):
    return sueldo*12

def calcular_bono(sueldo_anual):
    if sueldo_anual >= 40000:
        porcentaje = 10
        bono_calculado = sueldo_anual*porcentaje*1/100
        
    else:
        porcentaje = 5
        bono_calculado = sueldo_anual*porcentaje*1/100

    return porcentaje,bono_calculado

sueldo_anual_1 = calcular_sueldo_anual(empleado1["sueldo"])
sueldo_anual_2 = calcular_sueldo_anual(empleado2["sueldo"])

porcentaje1,bono1 =calcular_bono(sueldo_anual_1)
porcentaje2,bono2 =calcular_bono(sueldo_anual_2)

print("Nombre: ",empleado1["nombre"])
print("Sueldo Anual: S/",sueldo_anual_1)
print("Porcentaje bono: ",porcentaje1)
print("Monto del bono: S/",bono1)
print("================================")

print("Nombre: ",empleado2["nombre"])
print("Sueldo Anual: S/",sueldo_anual_2)
print("Porcentaje bono: ",porcentaje2)
print("Monto del bono: S/",bono2)
    