cad1 = input("Dime una cadena: ")
cad2 = input("Dime otra cadena: ")
if cad2.lower() in cad1.lower():
    print("La segunda cadena es una subcadena de la primera.")
else:
    print("La segunda cadena no es una subcadena de la primera.")