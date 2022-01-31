actual=int(input("¿En qué año estamos?: "))
while actual <= 0:
    print("Error. Introduzca un número positivo.")
    actual=int(input("¿En qué año estamos?: "))
otro=int(input("Escriba un año cualquiera: "))
while otro <= 0:
    print("Error. Introduzca un número positivo.")
    actual=int(input("¿En qué año estamos?: "))
    otro=int(input("Escriba un año cualquiera: "))
if actual < otro:
    futuro = otro - actual
    print("Para llegar al año",otro,"faltan",futuro,"años.")
    if futuro == 1:
        print("Para llegar al año",otro,"falta",futuro,"año.")
elif actual > otro:
    pasado = actual - otro
    print("Desde el año",otro,"han pasado",pasado,"años.")
    if pasado == 1:
        print("Desde el año",otro,"ha pasado",pasado,"año.")
elif actual == otro:
    print("¡Son el mismo año!")