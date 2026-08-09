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
    }
}

def obtener_area(empleados, nombre):

    empleado = empleados.get(nombre)

    if empleado is None:
        return "Empleado no encontrado"

    return empleado.get("area", "Área no asignada")


print(obtener_area(empleados, "Tom"))
print(obtener_area(empleados, "Carlos"))