cad = input("Introduce una cadena: ")
while len(cad) < 1:
    print("¡No has introducido ninguna cadena!")
    cadena = input("Introduce una cadena: ")
repe = 0
for i in cad:
    if cad.count(i) > 1:
        repe = repe +1
if repe == 0:
    print("No tiene carácteres repetidos.")
else:
    print("Mínimo se ha repetido un carácter.")