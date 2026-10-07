"""
====================================================================
Mi Primera Función en Turtle
====================================================================
NOMBRE: Gabriela Torrellas
Objetivo: Aprender a crear y utilizar funciones en Turtle para dibujar figuras geométricas.
Entender cómo encapsular código en una función para reutilizarlo y 
dibujar figuras personalizadas de manera sencilla.

Corre este programa y toma captura del resultado
====================================================================
"""

import turtle

# ==================================================================
# 1. Configuración de la Pantalla y Tortuga
# ==================================================================
pantalla = turtle.Screen()
pantalla.bgcolor("lightyellow")
pantalla.title("Funciones y Figuras")

t = turtle.Turtle()
t.shape("turtle")
t.speed(3)


# ==================================================================
# 2. DEFINICIÓN DE LA FUNCIÓN
# ==================================================================

# Función para 
def dibujar_figura(lados, tamaño, color_borde, color_relleno):
    """
    Dibuja cualquier polígono regular basado en el número de lados.
    
    Parámetros:
    - lados: Número de lados que tendrá la figura (ej. 3 para triángulo, 5 para pentágono).
    - tamaño: Longitud de cada lado en píxeles.
    - color_borde: Color de las líneas.
    - color_relleno: Color del interior de la figura.
    """
    
    # La suma de los ángulos exteriores de cualquier polígono es 360 grados.
    angulo = 360 / lados

    # Configuración de colores
    t.color(color_borde, color_relleno)
    t.begin_fill()

    # Un bucle 'for' que repita el avance y el giro 'lados' veces.
    for _ in range(lados):
        t.forward(tamaño)
        t.left(angulo)

    t.end_fill()


# Función auxiliar para 
def mover(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


# ==================================================================
# 3. DEMOSTRACIÓN / PRUEBAS (Demuestra el poder de la función)
# ==================================================================

# Dibujar una estrella/triángulo (3 lados)
mover(-150, 0)
dibujar_figura(lados=3, tamaño=80, color_borde="darkgreen", color_relleno="lightgreen")

# Dibujar un pentágono (5 lados)
mover(0, 0)
dibujar_figura(lados=5, tamaño=60, color_borde="purple", color_relleno="plum")

# Dibujar un hexágono (6 lados)
mover(150, 0)
dibujar_figura(lados=6, tamaño=50, color_borde="darkblue", color_relleno="skyblue")

mover(-150, -150)
t.color("red", "pink")
t.begin_fill()
for _ in range(4):
    t.forward(80)
    t.left(90)
t.end_fill()


# ==================================================================
# 4. PREGUNTAS
# ==================================================================
"""
1.  ¿Cuantas funciones hay en este programa? Que proposito tienen? En tus propias palabras agrega comentario completo.
# R: Hay dos funciones en este programa. La primera es 'dibujar_figura', que se encarga de dibujar cualquier polígono regular basado en el número de lados, tamaño y colores especificados. La segunda es 'mover', que permite mover la tortuga a una posición específica en la pantalla sin dibujar.

2. ¿Qué parámetro de la función 'dibujar_figura' tendrías que cambiar para hacer un octágono (8 lados)?
# R: El parámetro 'lados' debería cambiarse a 8.

3 ¿En que numero de linea termina la funcion mover?
# R: La función 'mover' termina en la línea 62.

4. Bajo la seccion de pruebas, intenta hacer una nueva figura sin el uso de la funcion dibujar_figura.
# R: Se puede dibujar un cuadrado manualmente usando t.forward() y t.left() cuatro veces, por ejemplo:
#
# mover(-150, -150)
# t.color("red", "pink")
# t.begin_fill()
# for _ in range(4):
#     t.forward(80)
#     t.left(90)
# t.end_fill()

5. Guarda una captura de pantalla con las 4 figuras en la carpeta M06.
      
"""


pantalla.exitonclick()