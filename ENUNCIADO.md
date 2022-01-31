# Ejercicios repetitivas y alternativas

# Ejercicio 1

Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año. Se puede mejorar el programa haciendo que cuando la diferencia sea exactamente un año y escriba la frase en singular.

# Ejercicio 2

Juego de las multiplicaciones

## Apartado 1

Escriba un programa que genere una multiplicación de dos números del 2 al 10 al azar, pregunte por el resultado y diga si se ha dado la respuesta correcta.

Para generar números al azar puedes utilizar el siguiente código:

from random import randint
a = randint(2, 10)

## Apartado 2

Amplie el programa anterior haciendo que el programa pida primero al usuario cuántas multiplicaciones se van a plantear.

## Apartado 3

Amplíe el programa anterior haciendo que el programa lleve la cuenta de las respuestas correctas e incorrectas e indique la nota correspondiente. Si la nota es igual o mayor que 9, el programa felicitará al usuario por el resultado. 

Ayuda: La nota se calcula con la fórmula Nota=Correctas / Total * 10.

NOTA: Tienes que entregar sólo el código del apartado 3.

# Ejercicios cadenas

# Ejercicio 3

Para calcular la letra del DNI se calcula el número del DNI módulo 23 y el resultado es la posición en la siguiente cadena:

'TRWAGMYFPDXBNJZSQVHLCKE'

Crear un programa que pida un DNI (valide que tiene 9 caracteres) y diga si es válido.

# Ejercicio 4

Realiza un programa que pida un cadena. A continuación debe pedir otra cadena. El programa debe buscar la segunda cadena en la primera (ignorando mayúsculas o minúsculas) y podrá responder una de las siguientes opciones:

* La segunda cadena es una subcadena de la primera
* La segunda cadena no es una subcadena de la primera

# Ejercicio 5

Escribe una programa que pida una cadena de caracteres y diga si no tiene caracteres repetidos.
