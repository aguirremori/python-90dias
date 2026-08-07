empleados = [
    {
        "nombre" : "Tom",
        "cargo" : "Planning Manager",
        "sueldo" : 8500
    },

    {
        "nombre" : "Laura",
        "cargo" : "Supervisor",
        "sueldo" : 5200
    },

    {
        "nombre" : "Pedro",
        "cargo" : "Operario",
        "sueldo" : 2500
    }
]

total_planilla = 0

for empleado in empleados :
    # print(empleado["nombre"])

    # print(f"{empleado['nombre']} - {empleado["cargo"]}")

    # print(f"{empleado["nombre"]} gana S/ {empleado["sueldo"]}")

    total_planilla += empleado["sueldo"]

print(f"Total planilla: S/ {total_planilla}")