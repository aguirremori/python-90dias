import json

listado_productos = [{"codigo":"P001","nombre":"Laptop","precio": 2500,"stock":10},
                    {"codigo":"P002","nombre":"Mouse","precio": 80,"stock":25},
                    {"codigo":"P003","nombre":"Teclado","precio": 120,"stock":15}
                    ]

with open("productos.json","w") as archivo:
    json.dump(listado_productos,archivo)

with open("productos.json","r") as archivo:
    lista = json.load(archivo)

print("PRODUCTOS")
print("----------------")
for item in lista:
    print("Codigo: ",item["codigo"])
    print("Nombre: ",item["nombre"])
    print("Precio: ",item["precio"])
    print("Stock: " ,item["stock"])
    print("\n")
    
