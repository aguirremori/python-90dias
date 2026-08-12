roles_permitidos = ["Administrador", "Supervisor", "Vendedor", "Almacenero"]

rol = "Cliente"

if rol in roles_permitidos:
    print("Rol autorizado")

else:
    print("Rol no autorizado")