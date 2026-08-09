empleados = {"Tom" : {"sueldo": 8500,
                      "area": "Planeamiento" },
             "Laura":{"sueldo": 5200,
                      "area": "Logistica"},
             "Pedro":{"sueldo": 2500,
                      "area": "Produccion"}
}

print(list(empleados.keys())[0])
print(empleados["Tom"]["sueldo"])
print(empleados["Tom"]["area"])

print(empleados["Pedro"]["area"])