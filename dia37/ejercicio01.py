import json

producto = {
    "codigo": "P001",
    "nombre": "Laptop",
    "precio": 2500,
    "stock": 10
}

datos_json = json.dumps(producto)

print(datos_json)