empleados = [
    {"nombre": "Tom", "sueldo": 8500, "bono": 500},
    {"nombre": "Laura", "sueldo": 5200, "bono": 300},
    {"nombre": "Pedro", "sueldo": 2500, "bono": 200},
    {"nombre": "Carlos", "sueldo": 4000, "bono": 0},
    {"nombre": "Ana", "sueldo": 3200, "bono": 400}
]

def calcular_planilla(empleados):

    resultados = []

    for empleado in empleados:

        sueldo = empleado["sueldo"]
        bono = empleado["bono"]

        bruto = sueldo + bono
        afp = bruto * 0.13
        neto = bruto - afp

        resultado = {
            "nombre": empleado["nombre"],
            "bruto": bruto,
            "afp": afp,
            "neto": neto
        }
        
        resultados.append(resultado)

    return resultados

planilla = calcular_planilla(empleados)

for empleado in planilla:
    print(
        f"Nombre: {empleado['nombre']} | "
        f"Bruto: {empleado['bruto']} | "
        f"AFP: {empleado['afp']} | "
        f"Neto: {empleado['neto']}"
    )