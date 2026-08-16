import json

empleados =[ {
    "codigo": "P001",
    "nombre": "Tom",
    "rol":    "Supervisor",
    "sueldo":  3500},
{
    "codigo": "P002",
    "nombre": "Liam",
    "rol":    "Gerente",
    "sueldo":  8500},
{
    "codigo": "P003",
    "nombre": "Leo",
    "rol":    "Administrador",
    "sueldo":  5500}
    ]

datos_json = json.dumps(empleados)

print(datos_json)