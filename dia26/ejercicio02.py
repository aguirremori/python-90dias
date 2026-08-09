empleados = [
    {"nombre": "Tom", "sueldo": 8500},
    {"nombre": "Laura", "sueldo": 5200},
    {"nombre": "Pedro", "sueldo": 2500},
    {"nombre": "Carlos", "sueldo": 4000},
    {"nombre": "Ana", "sueldo": 3200}
]

def contar_empleados(empleados):
    contar = 0

    for empleado in empleados:
        if empleado["sueldo"] < 4000:
            contar+=1
    return contar

print(contar_empleados(empleados))