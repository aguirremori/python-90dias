productos = {
    "P001": {"nombre": "Laptop", "precio": 2500},
    "P002": {"nombre": "Mouse", "precio": 80},
    "P003": {"nombre": "Teclado", "precio": 120},
    "P004": {"nombre": "Monitor", "precio": 900}
}

codigo="P010"

if codigo in productos:
    print("Producto encontrado")

else:
    print("Producto no encontrado")
