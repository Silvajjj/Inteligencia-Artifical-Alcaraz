# Dataset: 30 Dudas Comunes de Python para Principiantes
dataset_python = [
    {"id": 1, "pregunta": "¿Qué es Python y por qué es bueno para empezar?", "respuesta": "Es un lenguaje de alto nivel, fácil de leer porque su sintaxis se parece al inglés. Es ideal para principiantes porque no requiere configurar cosas complejas para empezar a escribir código."},
    {"id": 2, "pregunta": "¿Por qué mi variable '1er_numero' marca error?", "respuesta": "En Python, los nombres de las variables no pueden empezar con números. Deben empezar con una letra o un guion bajo (_)."},
    {"id": 3, "pregunta": "¿Qué diferencia hay entre un entero (int) y un flotante (float)?", "respuesta": "Un 'int' es un número entero (ej. 5), mientras que un 'float' tiene decimales (ej. 5.0 o 3.14)."},
    {"id": 4, "pregunta": "¿Para qué sirve la función input()?", "respuesta": "Sirve para pedirle información al usuario a través del teclado. Ten en cuenta que todo lo que recibe lo guarda como texto (string)."},
    {"id": 5, "pregunta": "¿Cómo convierto un texto a número?", "respuesta": "Usando las funciones int() o float(). Ejemplo: numero = int(\"25\")."},
    {"id": 6, "pregunta": "¿Qué hace el operador módulo (%)?", "respuesta": "No calcula el porcentaje; te da el 'residuo' de una división. Por ejemplo, 10 % 3 es 1, porque 3 cabe tres veces en 10 y sobra 1."},
    {"id": 7, "pregunta": "¿Qué es un 'string'?", "respuesta": "Es una cadena de caracteres, básicamente cualquier texto encerrado entre comillas simples (' ') o dobles (\" \")."},
    {"id": 8, "pregunta": "¿Cómo puedo saber cuántos elementos tiene una lista?", "respuesta": "Usando la función len(). Ejemplo: len(mi_lista)."},
    {"id": 9, "pregunta": "¿Qué es un 'f-string'?", "respuesta": "Es una forma moderna de insertar variables dentro de un texto. Se escribe como f\"Hola {nombre}\"."},
    {"id": 10, "pregunta": "¿Por qué las listas empiezan en el índice 0?", "respuesta": "Es una convención en programación. El primer elemento está en la posición 0, el segundo en la 1, y así sucesivamente."},
    {"id": 11, "pregunta": "¿Cuál es la diferencia entre una lista [] y una tupla ()?", "respuesta": "Las listas se pueden modificar (agregar o quitar elementos), las tuplas son 'inmutables', una vez creadas no cambian."},
    {"id": 12, "pregunta": "¿Cómo agrego un elemento al final de una lista?", "respuesta": "Usando el método .append(). Ejemplo: lista.append(\"nuevo elemento\")."},
    {"id": 13, "pregunta": "¿Qué hace el error 'IndexError: list index out of range'?", "respuesta": "Significa que intentas acceder a una posición que no existe. Por ejemplo, pedir el elemento 5 de una lista que solo tiene 3 cosas."},
    {"id": 14, "pregunta": "¿Para qué sirve el bucle 'for'?", "respuesta": "Se usa para repetir una acción sobre cada elemento de una colección (como una lista o un rango de números)."},
    {"id": 15, "pregunta": "¿Cuándo debo usar un bucle 'while'?", "respuesta": "Cuando no sabes cuántas veces se repetirá la acción, pero quieres que continúe mientras una condición sea verdadera."},
    {"id": 16, "pregunta": "¿Qué es un 'Booleano'?", "respuesta": "Es un tipo de dato que solo puede tener dos valores: True (Verdadero) o False (Falso)."},
    {"id": 17, "pregunta": "¿Qué hace el comando 'break' dentro de un bucle?", "respuesta": "Detiene el bucle por completo inmediatamente, sin importar si faltaban vueltas por dar."},
    {"id": 18, "pregunta": "¿Qué hace 'continue' en un bucle?", "respuesta": "Salta la vuelta actual y pasa directamente a la siguiente repetición del bucle."},
    {"id": 19, "pregunta": "¿Cómo se define una función en Python?", "respuesta": "Usando la palabra reservada 'def' seguida del nombre de la función y paréntesis. Ejemplo: def mi_funcion():"},
    {"id": 20, "pregunta": "¿Cuál es la diferencia entre print() y return?", "respuesta": "print() muestra algo en pantalla para que el humano lo vea; return devuelve un valor para que el programa lo use después."},
    {"id": 21, "pregunta": "¿Qué es un diccionario en Python?", "respuesta": "Es una estructura que guarda datos en pares de 'llave: valor', como un diccionario real donde buscas una palabra (llave) y obtienes su definición (valor)."},
    {"id": 22, "pregunta": "¿Cómo se comentan líneas de código?", "respuesta": "Usando el símbolo de gato (#) para una sola línea o comillas triples para varias líneas."},
    {"id": 23, "pregunta": "¿Qué es la indentación?", "respuesta": "Es el espacio al inicio de las líneas de código. En Python es obligatorio para definir qué código va dentro de un if, for o función."},
    {"id": 24, "pregunta": "¿Qué significa 'None' en Python?", "respuesta": "Es un valor especial que representa la ausencia de valor o un valor nulo."},
    {"id": 25, "pregunta": "¿Cómo se importa una librería?", "respuesta": "Usando la palabra 'import'. Ejemplo: import math."},
    {"id": 26, "pregunta": "¿Qué es un 'SyntaxError'?", "respuesta": "Es un error de escritura. Significa que escribiste algo que Python no entiende (como olvidar dos puntos o cerrar un paréntesis)."},
    {"id": 27, "pregunta": "¿Cómo puedo generar un número aleatorio?", "respuesta": "Importando la librería random y usando funciones como random.randint(1, 10)."},
    {"id": 28, "pregunta": "¿Qué hace el operador '!='?", "respuesta": "Significa 'diferente de'. Se usa para comparar si dos valores no son iguales."},
    {"id": 29, "pregunta": "¿Para qué sirven los operadores 'and' y 'or'?", "respuesta": "Son operadores lógicos. 'and' requiere que dos condiciones sean ciertas; 'or' solo requiere que una de las dos sea cierta."},
    {"id": 30, "pregunta": "¿Cómo puedo leer un archivo de texto?", "respuesta": "Usando la función open() junto con el comando 'with' para asegurar que el archivo se cierre correctamente."}
]

# Script de ejecución
print(f"{'='*50}\n TUTOR DE PYTHON: 30 PREGUNTAS DE PRUEBA \n{'='*50}")
for duda in dataset_python:
    print(f"\nPregunta #{duda['id']}: {duda['pregunta']}")
    print(f"Respuesta: {duda['respuesta']}")

    