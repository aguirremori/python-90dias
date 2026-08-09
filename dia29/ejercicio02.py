import pprint

empleados = {
    "Tom": {
        "sueldo": 9000,
        "area": "Planeamiento",
        "bono": 500
    },
    "Laura": {
        "sueldo": 5200,
        "area": "Logistica",
        "bono": 0
    },
    "Pedro": {
        "sueldo": 2500,
        "area": "Produccion",
        "bono": 200
    }
}

for nombre, datos in empleados.items():
    pprint.pprint(datos)
