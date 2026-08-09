empleados = [
    {"nombre": "Tom", "sueldo": 8500, "area": "Planeamiento"},
    {"nombre": "Laura", "sueldo": 5200, "area": "Logistica"},
    {"nombre": "Pedro", "sueldo": 2500, "area": "Produccion"},
    {"nombre": "Carlos", "sueldo": 4000, "area": "Planeamiento"},
    {"nombre": "Ana", "sueldo": 3200, "area": "Produccion"}
]

def empleados_por_area(empleados,area):
    empleados_area = [] 

    for empleado in empleados:
        if empleado["area"] == area:
            empleados_area.append(empleado)
    return empleados_area

print(empleados_por_area(empleados,"Produccion"))