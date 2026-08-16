import json

with open("productos.json","r") as archivo:
    items = json.load(archivo)

codigo_buscar = "P001"

encontrado = False

for item in items:
    if item["codigo"]==codigo_buscar:
        encontrado = True
        print("Producto encontrado")
        print("Nombre: ",item["nombre"])
        print("Precio: S/",item["precio"])
        print("Stock: ",item["stock"])
 
if not encontrado:
    print("Producto no encontrado")