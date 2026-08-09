empleados = {
    "Tom": {
        "sueldo": 8500,
        "area": "Planeamiento",
        "bono": 500
    },
    "Laura": {
        "sueldo": 5200,
        "area": "Logistica"
    },
    "Pedro": {
        "sueldo": 2500,
        "area": "Produccion",
        "bono": 200
    }
}

for nombre,values in empleados.items():

    values.setdefault("bono",0)

    # if nombre == "Tom":
    #     values["sueldo"] += 500 

empleados["Tom"]["sueldo"] += 500

empleados["Pedro"].pop("bono",0)

print(empleados)