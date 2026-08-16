import json

with open("productos.json","r") as archivo:
    productos = json.load(archivo)

codigo="P003"
nuevo_stock=500

def actualizar_stock(productos,codigo,nuevo_stock):

    for producto in productos:
        if producto["codigo"]==codigo:
            producto["stock"]=nuevo_stock
            return True
    return False


actualizar_stock(productos,codigo,nuevo_stock)

with open("productos.json","w") as archivo:
    json.dump(productos,archivo)