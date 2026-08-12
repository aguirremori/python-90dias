ventas = [120, 450, 80, 700, 300, 50]

i=0
suma=0
while i < len(ventas):
    if ventas[i] >= 300:
        suma+=ventas[i]
    i+=1

print("Total de ventas >=300: S/",suma)   