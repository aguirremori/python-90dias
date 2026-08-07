empleados = ["Carlos","Laura","Pedro","Luis"]

print(empleados[0])
print(empleados[3])

empleados[1]="Tom"

print(empleados)

empleados.append("Raquel")
empleados.append("Leonardo")

print(empleados)
print("\n")

for empleado in empleados:
    print("Empleado :",empleado)