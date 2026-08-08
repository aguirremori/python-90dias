# def es_mayor_edad(edad):
#   return edad >= 18

# resultado = es_mayor_edad(15)

# print(resultado)

# def calcular_bono(sueldo):
#     if sueldo >=5000:
#         return 500

#     return 200

# print(calcular_bono(7000))
# print(calcular_bono(3000))

def categoria_empleado(sueldo):
    if sueldo >= 7000:
        return "Gerencia"

    if sueldo >=4000:
        return "Supervisor"

    return "Operario"

print(categoria_empleado(8500))
print(categoria_empleado(5200))
print(categoria_empleado(2500))