import empleados.datos
import empleados.calculos
import empleados.reportes

import productos.datos
import productos.inventario

# datos_empleado = empleados.datos.obtener_empleado()
# sueldo = datos_empleado["sueldo"]
# sueldo_anual = empleados.calculos.calcular_sueldo_anual(sueldo)
# empleados.reportes.mostrar_resumen(datos_empleado,sueldo_anual)

lista_productos = productos.datos.obtener_productos()

producto = productos.inventario.buscar_producto(lista_productos,"P003")

if producto !=None:
    print("Producto encontrado:")
    print("Codigo: ", producto["codigo"])
    print("Nombre: ", producto["nombre"])
    print("Precio: ", producto["precio"])
    print("Stock: ", producto["stock"])

else:
    print("Producto no encontrado")