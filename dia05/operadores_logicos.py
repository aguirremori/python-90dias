nombre = input("Ingrese su nombre: ")
cargo = input("Ingrese su cargo: ")
sueldo = float(input("Ingrese su sueldo: S/ "))
horas_extra = int(input("Ingrese sus horas extras: "))

if (cargo.lower() == "gerente" or cargo.lower() == "supervisor") and sueldo > 5000:
    print("Empleado con acceso VIP.")

elif horas_extra >20:
       print("Empleado con bono por horas extras")

else:
      print("Empleado estandar")