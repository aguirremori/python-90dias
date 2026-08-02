#Ejercicio 01

# def calcular_producto(precio,cantidad):
#     subtotal = precio*cantidad
#     igv = subtotal*0.18

#     return subtotal,igv

# subtotal,igv = calcular_producto(120,3)

# print("Subtotal:",subtotal)
# print("IGV:",igv)

#Ejercicio 02

def datos_empleado():
    nombre ="Carlos"
    cargo = "Supervisor"
    edad = 35

    return nombre,cargo,edad

nombre,cargo,edad = datos_empleado()

print(nombre)
print(cargo)
print(edad)
