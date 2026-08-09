empleados = [
    {"nombre": "Tom", "sueldo": 8500},
    {"nombre": "Laura", "sueldo": 5200},
    {"nombre": "Pedro", "sueldo": 2500},
    {"nombre": "Carlos", "sueldo": 4000},
    {"nombre": "Ana", "sueldo": 3200}
]

def buscar_empleado(empleados,nombre):

    for empleado in empleados:
        if empleado["nombre"] == nombre:
            return empleado

    return None

print(buscar_empleado(empleados,"Anas"))