empleados = [
    {
        "nombre": "Tom",
        "cargo": "Planning Manager",
        "sueldo": 8500
    },
    {
        "nombre": "Laura",
        "cargo": "Supervisor",
        "sueldo": 5200
    },
    {
        "nombre": "Pedro",
        "cargo": "Operario",
        "sueldo": 2500
    },
    {
        "nombre": "Carlos",
        "cargo": "Ingeniero",
        "sueldo": 6200
    }
]

sueldo_ingresado = int(input("Ingrese sueldo minimo: "))

encontrado = False

for empleado in empleados:
    if empleado["sueldo"] > sueldo_ingresado:
        print(f"{empleado["nombre"]} - {empleado['sueldo']}")
        encontrado = True

if not encontrado:
    print(f"No existen empleados con sueldo mayor a S/ {sueldo_ingresado}")