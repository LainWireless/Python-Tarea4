from random import randint
preguntas = int(input("Número de preguntas: "))
total = preguntas
correctas = 0
while preguntas < 1:
    print("Error. El número de preguntas debe ser al menos 1.")
    preguntas = int(input("Número de preguntas: "))
while preguntas > 0:
    a = randint(2, 10)
    b = randint(2, 10)
    respuesta = int(input("¿Cuánto es %i por %i?: " %(a,b)))
    preguntas = preguntas -1
    resultado = a*b
    if respuesta == resultado:
        print("Respuesta correcta.")
        correctas = correctas +1
    else:
        print("Respuesta incorrecta.")
nota = correctas / total * 10
if correctas == 1:
    print("Ha contestado correctamente",correctas,"pregunta.")
elif correctas == 0:
    print("No ha contestado correctamente ninguna pregunta.")
else:
    print("Ha contestado correctamente",correctas,"preguntas.")
print("Le corresponde una nota de",nota)
if nota >= 9:
    print("¡Enhorabuena!")