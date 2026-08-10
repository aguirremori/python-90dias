sueldos = [2500, 3500, 2800, 4200, 3000, 1800, 5000]

i = 0

while i < len(sueldos):
    if sueldos[i] < 3000:
        i = i+1
        continue
    if sueldos[i]>=5000:
        print(sueldos[i])
        break
    print(sueldos[i])
    i = i+1