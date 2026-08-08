def calcular_afp(sueldo):
    if sueldo >= 3000:
        descuento = sueldo*0.13
        
    else:
        descuento = sueldo*0.11

    neto = sueldo - descuento

    return {
        "sueldo" : sueldo,
        "descuento" : descuento,
        "neto" : neto
    }

print(calcular_afp(5000))