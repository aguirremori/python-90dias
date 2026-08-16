import json

with open("producto.json","r") as archivo:
    producto = json.load(archivo)

print("Codigo: ",producto["codigo"])
print("Nombre: ",producto["nombre"])
print("Precio : S/",producto["precio"])
print("Stock: ",producto["stock"])