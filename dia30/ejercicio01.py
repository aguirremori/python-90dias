empleados = {
    "E001": {
        "nombre": "Carlos",
        "cargo": "Analista",
        "sueldo": 3500
    },
    "E002": {
        "nombre": "Maria",
        "cargo": "Supervisora",
        "sueldo": 4800
    },
    "E003": {
        "nombre": "Jose",
        "cargo": "Tecnico",
        "sueldo": 2800
    },
    "E004": {
        "nombre": "Ana",
        "cargo": "Analista",
        "sueldo": 3700
    }
}

def mostrar_empleados(empleados):
    for codigo,empleado in empleados.items():
        print(f"{codigo} - {empleado["nombre"]} - {empleado["cargo"]} - S/ {empleado["sueldo"]}")

def buscar_empleado(empleados,codigo):

    encontrado = False
    for codigo_empleado,empleado in empleados.items():
        if codigo_empleado == codigo:
            encontrado = True
            print("Empleado encontrado")
            print("Nombre: ",empleado["nombre"])
            print("Cargo: ", empleado["cargo"])
            print("Sueldo: S/", empleado["sueldo"])
    if encontrado == False:
        print("Empleado no encontrado")

def calcular_total_sueldos(empleados):

    total_sueldos = 0

    for empleado in empleados.values():
        total_sueldos += empleado["sueldo"]
    return total_sueldos

print("========SISTEMA DE EMPLEADOS==========")
print("1.Mostrar empleados")
print("2.Buscar empleado")
print("3.Mostrar total de sueldos")
print("4.Salir")

opcion = int(input("Ingrese la opcion a elegir: "))

if opcion == 1:
   mostrar_empleados(empleados)
elif opcion == 2:
  codigo_empleado = input("ingrese el codigo del empleado: ")
  buscar_empleado(empleados,codigo_empleado)
elif opcion == 3:
    total = calcular_total_sueldos(empleados)
    print("Total de sueldos: S/",total)
elif opcion == 4:
    print("Programa finalizado")
else:
    print("Opcion no valida")

  