def calcular_descuento(total):
    if total > 1000:
        return total*0.1
    else:
        return total*0.05

print(calcular_descuento(1500))