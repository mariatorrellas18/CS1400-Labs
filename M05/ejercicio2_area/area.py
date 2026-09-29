"""
## 📗 Calcular el Área de Varios Círculos (Práctica de Iteraciones)

### Instrucciones:
1. Descomenta la linea que dejara importar el módulo math.
2. Crea una lista con los radios: [5, 12, -3, 8, 0].
3. Utiliza un bucle for para recorrer cada radio de la lista.
4. Dentro del bucle, usa un condicional if/else para calcular y mostrar el área únicamente si el radio es mayor que 0.
5. Reto de Iteración Continuada: Cambia la estructura a un bucle while que le pida al usuario radios continuamente con input() hasta que ingrese 'salir', calculando el área de cada radio válido o pidiendo el dato de nuevo si no es válido.

NOMBRE: [Tu Nombre]
MÓDULO 5 - EJERCICIO 2 (Adaptada)
ÁREA DE CÍRCULOS E ITERACIONES
Uso de bucles (for / while), listas, validación y estructuras de control.
"""

# importando el modulo math
# import math

# --- PARTE 1: Iteración sobre una lista de datos (FOR Loop) ---

radios = [5, 12, -3, 8, 0]
import math

print("--- Procesando lista de radios ---")

# TODO Tarea 1: Crea un bucle 'for' que recorra la lista 'radios' mira las palabras claves mas adelante para evitar errores.
for radio in radios:

    # TODO Tarea 2: Verifica con if/else si el radio es válido (mayor a 0).
    #
    if radio > 0:
        print(f"Calculando área para radio: {radio}")
        print(f"Radio: {radio}")
        print(f"Calculando área para radio: {radio}")
        area = math.pi * (radio ** 2)
        print(f"Área calculada: {area:.2f}")
        print(f"Radio: {radio} -> Área: {area:.2f}")
        print()  # Línea en blanco para separar cada cálculo
        continue  # Continúa con el siguiente radio de la lista
    else:
        print(f"Radio: {radio} -> Error: El radio debe ser mayor que cero.")
        print()  # Línea en blanco para separar cada cálculo de error


# --- PARTE 2: Iteración interactiva y continua (WHILE Loop) ---

print("\n--- Modo Interactivo (Escribe 'salir' para terminar) ---")

# TODO Reto: Completa el while loop para solicitar radios al usuario indefinidamente.
# Debe repetirse hasta que el usuario escriba 'salir'.
while True:
    radio_usuario = input("Ingresa el radio del círculo (o 'salir' para terminar): ")

    if radio_usuario.lower() == "salir":
        print("Finalizando el modo interactivo.")
        break  # Interrumpe la iteración

    try:
        radio_usuario = float(radio_usuario)

        # Validar si es positivo mediante iteración/condición
        if radio_usuario > 0:  # para evitar errores de matematica
            #entonces la matematica se hace igual que en la Parte 1
            area = math.pi * (radio_usuario ** 2)
            print(f"El área del círculo es: {area:.2f}\n")
        else:
            print("Error: El radio debe ser mayor que cero.\n")

    # Otra manera de encontrar errores del usuario. Descomenta las siguientes lineas al finalizar tu while loop.       
    except ValueError:
        print("Error: Por favor ingresa un número válido o la palabra 'salir'.\n")
        print()  # Línea en blanco para separar cada intento de entrada del usuario
        continue  # Continúa con el siguiente intento de entrada del usuario
