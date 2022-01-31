dni = input("Introduzaca un DNI: ")
while len(dni) != 9:
    print("Error. Introduzca 9 caracteres.")
    dni = input("Introduzaca un DNI: ")
letra = dni[8].upper()
numero = int(dni[:8])
posicion = numero%23
cadena = "TRWAGMYFPDXBNJZSQVHLCKE"
print("Para el número",numero,"la letra correspondiente es",cadena[posicion])
if cadena[posicion] == letra:
    print("DNI válido.")
else:
    print("DNI no válido.")