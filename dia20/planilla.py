
def total_planilla(empleados):
    total = 0
    for empleado in empleados:
        total += empleado["sueldo"]
    return total