productos = {
    "P001": {"nombre": "Laptop", "precio": 2500},
    "P002": {"nombre": "Mouse", "precio": 80},
    "P003": {"nombre": "Teclado", "precio": 120},
    "P004": {"nombre": "Monitor", "precio": 900}
}

codigo = input("Ingrese el codigo de producto: ")

if codigo in productos:
    print("Producto encontrado")
    print(productos[codigo]["nombre"])
    print(productos[codigo]["precio"])

else:
    print("Producto no encontrado")