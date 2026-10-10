# ==========================================
# TAREA Turtle 🐢
# ==========================================
# En esta actividad aprenderás a:
# 1. Mover la tortuga hacia adelante.
# 2. Girarla usando grados.
# 3. Dibujar un cuadrado.
# 4. Usar un bucle para repetir instrucciones.
#
# IMPORTANTE:
# - Un giro completo es de 360 grados.
# - Un cuadrado tiene 4 lados iguales.
# - Cada esquina de un cuadrado mide 90 grados.
#
# Completa todos los TODO.

# ------------------------------------------
# Importaciones necesarias
# ------------------------------------------

import turtle
# La siguiente linea agrega funciones para realizar la tarea en nuestro programa
#from turtle import make_turtle, forward, left


# ------------------------------------------
# Crear la ventana y la tortuga
# ------------------------------------------

# TODO 1
#  Iniciar ventana y objeto de tortuga y agregar el speed o velocidad. Pista: Mira la Tarea 1turtle.py

# Escribe aquí tu código
pantalla = turtle.Screen()
pantalla.bgcolor("lightyellow")
pantalla.title("Tortuguita Casa")

t = turtle.Turtle()
t.shape("turtle")
t.speed(3) 

# TODO 2
#  Crea la tortuga usando make_turtle().
#  La ventana debe tener 400 de alto y 400 de ancho.

# Escribe aquí tu código
pantalla.setup(width=400, height=400)

# Captura de Pantalla, nombralo "TUNOMBRE_1_2" y guardalo en la carpeta M06

# ------------------------------------------
# Dibujar una línea
# ------------------------------------------

# TODO 3:
# Mueve la tortuga hacia adelante 100 pasos.
# Observa qué sucede.


t.fillcolor("lightblue")
t.begin_fill()

t.forward(100)
# ------------------------------------------
# Girar la tortuga
# ------------------------------------------

# TODO 4:
# Gira la tortuga 90 grados hacia la izquierda.
# Luego avanza otros 100 pasos.

t.left(90)
t.forward(100)


# ------------------------------------------
# Dibujar un cuadrado 
# ------------------------------------------
# Un cuadrado tiene:
# - 4 lados
# - 4 giros de 90 grados

print("Dibujando un cuadrado...")

# TODO 5:
# Completa los movimientos necesarios
# para dibujar un cuadrado de lado 100.
# Debes usar forward() y left() varias veces.
# La tortuga debe terminar donde empezó.

t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.fillcolor("lightblue")

t.end_fill()

print("Cuadrado terminado")


# ------------------------------------------
# Paso EXTRA (opcional)
# ------------------------------------------
# ¿Puedes agregar un triángulo? y un rectangulo? Dibuja una casita.
#
# Pista:
# - Un triángulo tiene 3 lados.
# - Un giro completo es 360 grados.
# - ¿Cuánto debe girar en cada esquina?

# Dibujar el techo de la casa
# Dibujar el techo de la casa
print("Comenzando el techo")

t.penup()
t.goto(0, 100)
t.setheading(0)
t.pendown()

t.fillcolor("#FFDAB9")
t.begin_fill()

t.left(60)
t.forward(100)
t.right(120)
t.forward(100)
t.right(120)
t.forward(100)

t.end_fill()

print("Techo terminado")


# Dibujar una puerta
t.penup()
t.goto(35, 0)
t.setheading(90)
t.pendown()
# Pintar la puerta de amarillo claro
t.fillcolor("lightyellow")
t.begin_fill()

t.forward(50)
t.right(90)
t.forward(30)
t.right(90)
t.forward(50)
t.end_fill()

# Dibujar la ventana izquierda
t.penup()
t.goto(10, 60)
t.setheading(0)
t.pendown()

for i in range(4):
    t.forward(20)
    t.left(90)


# Dibujar la ventana derecha
t.penup()
t.goto(70, 60)
t.setheading(0)
t.pendown()
for i in range(4):
    t.forward(20)
    t.left(90)

print("¡La casa se dibujó completamente!")
pantalla.mainloop()

# Mantiene la ventana abierta hasta que hagas clic en ella
pantalla.exitonclick()
