import json

with open("productos.json","r") as archivo:
    productos = json.load(archivo)

codigo = "P005"

def buscar_producto(productos,codigo):
    
    for producto in productos:
        if producto["codigo"]==codigo:
            return producto
    
    return None

print(buscar_producto(productos,codigo))