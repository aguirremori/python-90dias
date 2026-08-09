empleado = {
    "nombre": "Tom",
    "sueldo": 9000,
    "area": "Produccion",
    "horas_extra": 10
}

del empleado["horas_extra"]

empleado.pop("bono",None)

print(empleado)