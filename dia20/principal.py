from funciones import saludar
from funciones import sumar
from funciones import calcular_igv
from planilla import total_planilla

# saludar("Tom")


# resultado = sumar(10,20)
# print(f"Resultado: {resultado}")


# igv=calcular_igv(2500)
# print(f"IGV: {igv}")

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

total = total_planilla(empleados)

print(f"Total planilla: S/ {total}")