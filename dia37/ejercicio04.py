import json

producto = {
    "codigo": "P001",
    "nombre": "Laptop",
    "precio": 2500,
    "stock": 10
}

with open("producto.json","w") as archivo:
    json.dump(producto,archivo)