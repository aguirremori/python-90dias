def calcular_afp(sueldo):
    if sueldo >= 3000:
        return sueldo*0.13
    else:
        return sueldo*0.11

print(calcular_afp(5000))