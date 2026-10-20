"""Tarea 1: Preparando la Oferta (Listas y Tuplas)

"""

# Tarea 1: Lista de elementos para el altar de muertos

# Lista de ofrendas editables (pueden agregarse o quitarse elementos)
ofrendas = ["Pan de muerto", "Flor de cempasúchil", "Velas", "Calaverita de azúcar"]

# Tupla con los niveles tradicionales del altar (constante, no debe cambiar)

NIVELES_ALTAR = ("Cielo", "Tierra", "Inframundo")

# Mostrar la segunda ofrenda (índice 1)
print("Segunda ofrenda:", ofrendas[1])
ofrendas.append("Incienso copal")
ofrendas.sort()
print(ofrendas)
# La lista ahora tiene un elemento nuevo y está ordenada
# alfabéticamente. Las posiciones de algunos elementos cambian.

#NIVELES_ALTAR[0] = "Gloria"
# Aparece un TypeError porque las tuplas son inmutables
# y no permiten modificar sus elementos.

for posicion, ofrenda in enumerate(ofrendas, start=1):
    print(posicion, ofrenda)

"""
Ejecuta el código. Observa qué elemento se imprime al pedir el índice 1.
#1. Modificación 1 (Listas): Agrega un nuevo elemento a la lista ofrendas usando
 .append("Incienso copal") y luego ordena la lista alfabéticamente usando
 la función .sort().  ¿Qué notas del variable en linea #12?

#2. Modificación 2 (Tuplas): Intenta modificar el primer elemento de la tupla escribiendo
 NIVELES_ALTAR[0] = "Gloria".
 ¿Qué sucede al ejecutar el código y por qué no permite realizar este cambio?

#3. Utiliza la función enumerate() dentro de un bucle for para imprimir cada ofrenda
 de tu lista junto con su número de posición en el altar.
"""

