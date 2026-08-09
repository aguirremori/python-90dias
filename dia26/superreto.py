empleados = [
    {"nombre": "Tom", "sueldo": 8500, "area": "Planeamiento"},
    {"nombre": "Laura", "sueldo": 5200, "area": "Logistica"},
    {"nombre": "Pedro", "sueldo": 2500, "area": "Produccion"},
    {"nombre": "Carlos", "sueldo": 4000, "area": "Planeamiento"},
    {"nombre": "Ana", "sueldo": 3200, "area": "Produccion"}
]

def resumen_area(empleados,area):

    total_sueldos = 0
    contador = 0

    for empleado in empleados:
            if empleado["area"] == area:
                total_sueldos += empleado["sueldo"]
                contador+=1

    if contador > 0:
         
        promedio = total_sueldos/contador

        return {
            "area" : area,
            "cantidad" : contador,
            "total_sueldos" : total_sueldos,
            "promedio" : promedio
            }

    else:
        return "Area no existente"

print(resumen_area(empleados,"Planeamiento"))
    
