empleados = [
    {"nombre": "Tom", "sueldo": 8500},
    {"nombre": "Laura", "sueldo": 5200},
    {"nombre": "Pedro", "sueldo": 2500},
    {"nombre": "Carlos", "sueldo": 4000},
    {"nombre": "Ana", "sueldo": 3200}
]

def analizar_empleados(empleados):
    total=0
    sueldo_promedio = 0
    mayor = 0
    cantidad = 0

    for empleado in empleados:
        total = total + empleado["sueldo"]
        if empleado["sueldo"] > mayor:
            mayor = empleado["sueldo"]
            nombre_mayor = empleado["nombre"]

        if empleado["sueldo"] < 4000:
            cantidad += 1
        
    sueldo_promedio = total/len(empleados)

    return {
        "total" : total,
        "promedio" : sueldo_promedio,
        "mayor_sueldo" : nombre_mayor,
        "cantidad_menor_4000" : cantidad
    }
print(analizar_empleados(empleados))
