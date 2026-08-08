empleados = [
    {"nombre": "Tom", "sueldo": 8500},
    {"nombre": "Laura", "sueldo": 5200},
    {"nombre": "Pedro", "sueldo": 2500}
]

# print(empleados[1]["nombre"])

# print(empleados[-1]["sueldo"])

# # empleados[-1]["sueldo"] = 3000

# print(empleados)

empleados.append({"nombre" : "Carlos", "sueldo" : 4000})

total_sueldos = 0

for empleado in empleados:
    total_sueldos +=empleado["sueldo"]

print(f"Total de sueldos: {total_sueldos}",)