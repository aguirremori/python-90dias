productos = {
    "P001": {"nombre": "Laptop", "precio": 2500},
    "P002": {"nombre": "Mouse", "precio": 80},
    "P003": {"nombre": "Teclado", "precio": 120},
    "P004": {"nombre": "Monitor", "precio": 900}
}

codigo = input("Ingrese codigo del producto:")

if codigo in productos:
    cantidad = int(input("Ingrese la cantidad a comprar: "))
    total = productos[codigo]["precio"]*cantidad

    print("Producto: ",productos[codigo]["nombre"])
    print("Precio: S/",productos[codigo]["precio"])
    print("Cantidad: ",cantidad)
    print("Total: S/",total)

else:
    print("Producto no encontrado")