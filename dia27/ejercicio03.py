empleados = {
    "Tom": {
        "sueldo": 8500,
        "area": "Planeamiento"
    },
    "Laura": {
        "sueldo": 5200,
        "area": "Logística"
    },
    "Pedro": {
        "sueldo": 2500,
        "area": "Producción"
    },
    "Carlos": {
        "sueldo": 4000,
        "area": "Planeamiento"
    },
    "Ana": {
        "sueldo": 3200,
        "area": "Producción"
    }
}

def analizar_area(empleados,area):

    total_sueldos = 0
    cantidad = 0

    for empleado in empleados.values():

        if empleado["area"] == area:

            total_sueldos += empleado["sueldo"]
            cantidad += 1

    if cantidad > 0:

        promedio = total_sueldos/cantidad

        return {
            "area": area,
            "cantidad": cantidad,
            "total_sueldos": total_sueldos,
            "promedio": promedio
        }

    else:
        return "Area no encontrada"

print(analizar_area(empleados,"ventas"))