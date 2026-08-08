def es_mayor_edad(edad):
    if edad <= 0:
        return "Edad invalida"

    elif edad >= 18:
        return True

    else:
        return False

print(es_mayor_edad(-2))
print(es_mayor_edad(10))
print(es_mayor_edad(18))
print(es_mayor_edad(35))