#Ejercicio 01

# def sumar_numeros(num1,num2):
#     return num1 + num2

# total = sumar_numeros(10,15)
# print("Resultado: ",total)

#Ejercicio 02

# def calcular_bruto(sueldo,bono):
#     return sueldo + bono

# bruto = calcular_bruto(4500,800)
# print("Sueldo bruto : S/",bruto)

#Ejercicio 03

def es_mayor_edad(edad):
    if edad >= 18:
        return True
    else:
        return False

if es_mayor_edad(17):
    print("Puede ingresar")
else:
    print("Acceso denegado")