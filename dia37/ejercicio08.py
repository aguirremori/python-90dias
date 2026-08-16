import json

with open("productos.json","r") as archivo:
    productos = json.load(archivo)

codigo_buscar = "P002"

for producto in productos:
    if producto["codigo"] == codigo_buscar:
        producto["stock"] = 20

with open("productos.json","w") as archivo:
    json.dump(productos,archivo)