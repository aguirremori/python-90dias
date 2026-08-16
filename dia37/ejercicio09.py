import json

with open("productos.json","r") as archivo:
    productos = json.load(archivo)

nuevo_producto = {"codigo":"P004","nombre":"Monitor","precio":900,"stock":8}

productos.append(nuevo_producto)

with open("productos.json","w") as archivo:
    json.dump(productos,archivo)