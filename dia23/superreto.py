def calcular_pago(sueldo):
    if sueldo < 0:
        return {
            "error" : "Sueldo invalido"
        }
    else:
        AFP = sueldo*0.13
        Neto = sueldo - AFP

        return {
            "sueldo":sueldo,
            "afp" : AFP,
            "neto": Neto
        }

print(calcular_pago(-100))
print(calcular_pago(10000))