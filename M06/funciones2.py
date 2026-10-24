
# =============================================================
# Parte 1: Funciones sin retorno (Acciones directas)
# =============================================================

def mostrar_bienvenida(nombre):
    """Muestra un mensaje de bienvenida con el nombre de la persona."""
    print(f"¡Hola, {nombre}! Bienvenido a clase hoy.")

# PREGUNTAS:
# 1. En la función mostrar_bienvenida(nombre), ¿cómo se llama la variable "nombre" dentro de los paréntesis?
# Respuesta: Se llama parámetro de la función.

# 2. ¿Qué le falta al código para ser completamente reutilizable?
# Respuesta: Le falta llamar a la función y pasarle diferentes nombres
# para poder usarla cuando la necesitemos.


# =============================================================
# Parte 2: Funciones con retorno (Procesamiento de datos)
# =============================================================

def calcular_descuento(precio, porcentaje=10):
    """Calcula el precio final después de aplicar un descuento."""
    precio = float(precio)
    descuento = precio * (porcentaje / 100)
    precio_final = precio - descuento
    return precio_final

def es_par(numero):
    """Verifica si un número es par y devuelve True o False."""
    return numero % 2 == 0

# PREGUNTAS:
# 3. ¿Qué palabra clave (keyword) de Python se utiliza para indicar que estamos definiendo una función?
# Respuesta: Se utiliza la palabra clave def.

# 4. Escribe los nombres de las dos funciones definidas arriba.
# Respuesta: calcular_descuento y es_par.

# 5. ¿Qué sucede cuando llamas a la función pasando solo un argumento, como calcular_descuento(100)?
# Respuesta: Se utiliza el descuento por defecto del 10%.
# El resultado sería 90.0.

# 6. ¿Qué ocurre si pasas dos argumentos, como calcular_descuento(200, 20)?
# Respuesta: Se aplica el descuento del 20% en lugar del 10%.
# El precio final sería 160.0.


# =============================================================
# Parte 3: Pruebas de ejecución
# =============================================================

print("--- PRUEBA 1: Mostrar Bienvenida ---")
mostrar_bienvenida("Ana")
mostrar_bienvenida("Carlos")

print("\n--- PRUEBA 2: Cálculo de Descuentos ---")

compra_1 = calcular_descuento(100)
print(f"Precio con descuento por defecto: ${compra_1}")


compra_2 = calcular_descuento(200, 20)
print(f"Precio con 20% de descuento: ${compra_2}")

# PREGUNTAS:
# 7. Escribe el pseudocódigo de las funciones en la Parte 2.
# Respuesta:
# Función calcular_descuento:
# Inicio
# Recibir el precio y el porcentaje de descuento.
# Si no se indica el porcentaje, utilizar 10%.
# Calcular el descuento multiplicando el precio por el porcentaje.
# Restar el descuento al precio original.
# Devolver el precio final.
# Fin
#
# Función es_par:
# Inicio
# Recibir un número.
# Dividir el número entre 2 y obtener el residuo.
# Si el residuo es 0, devolver True.
# Si no, devolver False.
# Fin

# 8. Explícale una de las dos a tu compañera(o) de al lado e incluye el propósito del programa. Tu compañera(o) te debe explicar lo siguiente. Lleguen a un acuerdo para agregar lo esencial como comentarios.
# Respuesta: La función calcular_descuento sirve para calcular el
# precio final de un producto después de aplicar un descuento.
# Recibe el precio y el porcentaje, calcula cuánto se descuenta
# y devuelve el precio final. Si no colocamos un porcentaje,
# utiliza automáticamente el 10%.
# La función es_par sirve para saber si un número es par.
# Devuelve True si es par y False si no lo es.

# 9. Cambia las funciones para que acepten decimales en el precio.
# Respuesta: Agregué float(precio) dentro de calcular_descuento
# para que pueda trabajar con precios decimales.
# La función es_par trabaja con números y no necesita un precio.

# Prueba con un precio decimal:
compra_decimal = calcular_descuento(99.99, 15)
print(f"Precio decimal con 15% de descuento: ${compra_decimal:.2f}")


# =============================================================
# Parte 4: Alcance (Scope) y Retorno
# =============================================================

# La función mostrar_bienvenida() usa print(), mientras que calcular_descuento() usa return.
# Si asignas la llamada de la bienvenida a una variable:

resultado = mostrar_bienvenida("Julio")
print(resultado)

# PREGUNTAS:
# 10. ¿Qué valor se guarda en la variable 'resultado' y por qué?
# Respuesta: Se guarda None porque la función solamente utiliza
# print() para mostrar el mensaje y no devuelve ningún valor.

# 11. ¿Por qué es necesario usar return en calcular_descuento() para poder guardar el precio final en compra_1 y compra_2?
# Respuesta: Porque return devuelve el resultado de la función
# y permite guardarlo en una variable para utilizarlo después.

# 12. Intenta ejecutar la siguiente línea al final del documento: print(descuento) ¿Qué error muestra Python?
# Respuesta: Muestra NameError: name 'descuento' is not defined.
# Esto sucede porque la variable solamente existe dentro de la función.

# 13. ¿Por qué la variable 'descuento' no es accesible fuera de la función?
# Respuesta: Porque es una variable local y solamente se puede
# utilizar dentro de la función donde fue creada.

# 14. ¿Qué ocurre si dentro de calcular_descuento cambias 'return precio_final' por 'print(precio_final)' e intentas sumar 'compra_1 + 5'?
# Respuesta: Aparece un TypeError porque print() solamente muestra
# el resultado, pero no lo devuelve. Entonces compra_1 sería None
# y no se puede sumar None con un número entero.

# 15. Investiga: ¿Cómo podrías llamar a la función 'calcular_descuento' asignando el porcentaje mediante su nombre de parámetro (keyword argument)?
# Respuesta: Podemos escribir el nombre del parámetro porcentaje
# cuando llamamos a la función, por ejemplo:

compra_3 = calcular_descuento(100, porcentaje=25)
print(f"Precio con 25% de descuento: ${compra_3}")

# 16. Añade un "docstring" (comentario multilínea con """) dentro de cada función para explicar brevemente qué hace.
# Respuesta: Agregué un docstring dentro de mostrar_bienvenida,
# calcular_descuento y es_par para explicar qué hace cada función.

# Prueba de la pregunta 12:
# print(descuento)
# La dejamos comentada para evitar que el programa se detenga.
