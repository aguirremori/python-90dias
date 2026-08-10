numeros = [15, 8, 22, 31, 10]

i=0
while i < len(numeros):
    if numeros[i] == 31:
        print(f"Numero encontrado en la posicion: {i}")
        break
    i=i+1