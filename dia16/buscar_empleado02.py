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

for empleado in empleados:
    if empleado["sueldo"] >5000:
        print(f"{empleado["nombre"]} - {empleado['sueldo']}")

