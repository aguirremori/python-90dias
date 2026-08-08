def calcular_pago(sueldo,dias):
    try:
        return sueldo/dias
    
    except ZeroDivisionError:
        return "No se puede calcular el pago"


print(calcular_pago(3000,30))
print(calcular_pago(3000,0))