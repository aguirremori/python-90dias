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

# for empleado in empleados :
#     print(empleado["nombre"])

name = input("Ingrese el nombre del empleado :").capitalize()

encontrado = False

for empleado in empleados :
    if empleado["nombre"] == name:
     print("Empleado encontrado")
     print(f"Nombre : {empleado["nombre"]}")
     print(f"Cargo : {empleado["cargo"]}")
     print(f"Sueldo : {empleado["sueldo"]}")
     encontrado =True

if not encontrado:
   print("Empleado no encontrado")
