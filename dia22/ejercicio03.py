def mensaje_stock(stock):
    if stock > 0:
        return "Stock disponible"
    else:
        return "Producto agotado"

print(mensaje_stock(0))