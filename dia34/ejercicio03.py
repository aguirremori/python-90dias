empleado = "E001,  Juan Perez  , Supervisor , 3500"

palabras = empleado.split(",")
palabras_limpias = []

for palabra in palabras:
    palabras_limpias.append(palabra.strip())

cadena = ",".join(palabras_limpias)

print(cadena)