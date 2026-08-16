import json

with open("productos.json","r") as archivo:
    productos = json.load(archivo)

codigo_buscar = "P004"

for posicion,producto in enumerate(productos):
    if producto["codigo"]==codigo_buscar:
        del productos[posicion]

with open("productos.json","w") as archivo:
    json.dump(productos,archivo)