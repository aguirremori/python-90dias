empleados = [
    {"nombre": "Tom","sueldo" : 8500},
    {"nombre" : "Laura", "sueldo" : 5200},
    {"nombre" : "Pedro", "sueldo" : 2500}
]

def buscar_empleado(empleados,nombre):
     
    for empleado in empleados:
        
     if empleado["nombre"] == nombre:
        return empleado
    
    return "Empleado no encontrado"

print(buscar_empleado(empleados,"Pedroh"))