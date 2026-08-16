import json

producto_json = '{"codigo": "P001", "nombre": "Laptop", "precio": 2500}'

diccionario_json = json.loads(producto_json)

print("Codigo: ",diccionario_json["codigo"])
print("Nombre: ",diccionario_json["nombre"])
print("Precio: ",diccionario_json["precio"])