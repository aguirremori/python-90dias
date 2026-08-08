def calcular_comision(ventas):
    if ventas < 0:
        return "Monto invalido"

    elif ventas < 10000:
        return ventas*0.05

    else:
        return ventas*0.08

print(calcular_comision(-1000))
print(calcular_comision(5000))
print(calcular_comision(150000))
