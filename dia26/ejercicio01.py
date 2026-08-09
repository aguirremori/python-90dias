empleados = [
    {"nombre": "Tom", "sueldo": 8500},
    {"nombre": "Laura", "sueldo": 5200},
    {"nombre": "Pedro", "sueldo": 2500},
    {"nombre": "Carlos", "sueldo": 4000},
    {"nombre": "Ana", "sueldo": 3200}
]

def filtrar_empleados(empleados):
    empleados_mayores = []

    for empleado in empleados:
        if empleado["sueldo"] >= 4000:
            empleados_mayores.append(empleado)
    return empleados_mayores

print(filtrar_empleados(empleados))