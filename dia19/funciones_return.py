empleados = [
    {
        "nombre":"Tom",
        "cargo":"Planning Manager",
        "sueldo":8500
    },
    {
        "nombre":"Laura",
        "cargo":"Supervisor",
        "sueldo":5200
    },
    {
        "nombre":"Pedro",
        "cargo":"Operario",
        "sueldo":2500
    }
]

def obtener_empleado(empleados,nombre):

    for empleado in empleados:
        if empleado["nombre"]==nombre:
            return empleado
    return None

resultado = obtener_empleado(empleados,"Pedro")

if resultado is None:
    print("Empleado no encontrado")

else:
    print(f"Nombre: {resultado["nombre"]}")
    print(f"Cargo:  {resultado["cargo"]}")
    print(f"sueldo: {resultado["sueldo"]}")