edades = [15, 22, 17, 30, 14, 25, 18, 12]

i=0
cantidad=0

while i < len(edades):
    if edades[i]>=18:
        cantidad+=1
    i+=1

print("Personas mayores de edad: ",cantidad)