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