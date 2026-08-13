empleado = "E001,Juan Perez,Supervisor,3500"

datos = empleado.split(",")

empleado_dict = { "codigo": datos[0],
                  "nombre": datos[1],
                  "rol":    datos[2],
                  "sueldo": int(datos[3]) 
                 }

print("Codigo: ", empleado_dict["codigo"])
print("Nombre: ", empleado_dict["nombre"])
print("Rol: ",    empleado_dict["rol"])
print("Sueldo: ", empleado_dict["sueldo"])
