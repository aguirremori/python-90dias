def calcular_planilla():
    try:
        sueldo = float(input("Ingrese sueldo :"))

        if sueldo < 0:
            return {"error" : "Sueldo invalido"}

        afp = sueldo*0.13
        neto = sueldo - afp

        return {
                "sueldo": sueldo,
                "afp" : afp,
                "neto" : neto
        }

    except ValueError:
        return "Debe ingresar un valor valido"


print(calcular_planilla())



