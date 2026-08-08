def calcular_envio(compra):

    if compra < 0:
        return "Monto invalido"

    elif compra >= 150:
        return 0

    else:
        return 15

print(calcular_envio(-1))
print(calcular_envio(100))
print(calcular_envio(150))