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
    }
]

def actualizar_sueldo(empleados,nombre,sueldo):
    for empleado in empleados:
        if empleado["nombre"] ==nombre:
            empleado["sueldo"] = sueldo

def mostrar_planilla(empleados):
    for empleado in empleados:
        print(f"{empleado["nombre"]}   {empleado["cargo"]}   {empleado["sueldo"]}")



def total_planilla(empleados):
    suma=0
    for empleado in empleados:
        suma+= empleado["sueldo"]
    return suma  

total = total_planilla(empleados)

print(total)
