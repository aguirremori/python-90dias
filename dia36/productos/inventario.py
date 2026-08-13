def buscar_producto(productos,codigo):
    
    for producto in productos:
        if producto["codigo"]==codigo:
            return producto
    
    return None
  
        