def calcular_bono(sueldo):
    if sueldo < 0:
        return "Monto invalido"
    
    elif sueldo < 3000:
        return 200

    else: 
        return 500

print(calcular_bono(-100))  
print(calcular_bono(2500))
print(calcular_bono(4500))