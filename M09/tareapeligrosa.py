def calculadora_segura():
    print("\n--- Calculadora Robusta ---")

    while True:
        try:
            n1 = float(input("Ingresa el primer número: "))
            n2 = float(input("Ingresa el segundo número: "))
            op = input("Operación (+, -, *, /): ")

            # Validar operador permitido
            if op not in ['+', '-', '*', '/']:
                raise ValueError("Operador no válido")

            # Realizar cálculos
            if op == '+':
                resultado = n1 + n2
            elif op == '-':
                resultado = n1 - n2
            elif op == '*':
                resultado = n1 * n2
            elif op == '/':
                resultado = n1 / n2

            print(f"Resultado: {resultado}")
            break

        except ZeroDivisionError:
            print("Error: No se puede dividir entre cero.")

        except ValueError as e:
            if str(e) == "Operador no válido":
                print(f"Error de entrada: {e}")
            else:
                print("Error: Ingrese valores numéricos válidos.")

        except Exception as e:
            print(f"Error no esperado: {e}")

        finally:
            print("Intento de cálculo finalizado.")


calculadora_segura()
# ============================================================
# TAREA: Tarea peligrosa
# Nombre: Gabriela Torrellas
# ============================================================

# PARTE 1: CÓDIGO VULNERABLE A ERRORES

# PREGUNTA 1:
# ¿Por qué la Operación 1 falla si el usuario ingresa 0?
# Respuesta:
# Porque no se puede dividir un número entre cero.
# Python genera un error llamado ZeroDivisionError.

# ¿Por qué la Operación 2 falla si el usuario ingresa 100?
# Respuesta:
# Porque la lista tiene solamente 4 elementos, con índices
# del 0 al 3. El índice 100 no existe y genera IndexError.


# PREGUNTA 2:
# ¿Qué resultados se obtienen en las tres pruebas?
# Respuesta:
# Entrada "dos": No continúa. Error: ValueError.
# Entrada 0: No continúa. Error: ZeroDivisionError.
# Entrada 100: No continúa. Error: IndexError.


# PREGUNTA 3:
# ¿Qué ocurre cuando Python encuentra un error no capturado?
# Respuesta:
# El programa se detiene inmediatamente y las siguientes
# líneas de código no se ejecutan.


# ============================================================
# PARTE 2: CONTROL DE FLUJO CON TRY / EXCEPT
# ============================================================

# PREGUNTA 4:
# ¿Qué ocurre al ingresar "dos"?
# Respuesta:
# Se imprime el mensaje:
# Error: Debes ingresar un número entero válido (sin letras).
# Sí, también se ejecuta la última línea que indica
# que el programa continúa normalmente.


# PREGUNTA 5:
# ¿Por qué al ingresar 0 aparece el error general?
# Respuesta:
# Porque ingresar 0 genera ZeroDivisionError y no ValueError.
# Como no existe un bloque específico para ese error,
# se ejecuta el except general.


# PREGUNTA 6:
# ¿Cómo se controla específicamente la división por cero?
# Respuesta:
# Se agrega un bloque except ZeroDivisionError para
# capturar ese error y mostrar el mensaje:
# Error: No es posible dividir entre cero.


# PREGUNTA 7:
# ¿Qué error ocurre al ingresar 100 y cómo se controla?
# Respuesta:
# Se genera IndexError porque el índice 100 no existe
# en la lista. Se agrega un bloque except IndexError
# para mostrar un mensaje indicando que el índice
# está fuera del rango permitido.


# PREGUNTA 8:
# ¿Cuáles son las tres excepciones específicas?
# Respuesta:
# ValueError: Captura entradas que no son números enteros.
# ZeroDivisionError: Captura divisiones entre cero.
# IndexError: Captura índices que no existen en la lista.
# Cada excepción muestra su propio mensaje de error.


# ============================================================
# PARTE 3: TRACEBACK, RAISE Y FINALLY
# ============================================================

# PREGUNTA 9:
# ¿Qué representa la variable e en except ValueError as e?
# Respuesta:
# La variable e guarda la excepción que ocurrió.
# Permite consultar el mensaje y los detalles del error.


# PREGUNTA 10:
# ¿Qué ventaja ofrece traceback.format_tb()?
# Respuesta:
# Permite ver información técnica del error, como
# el archivo, la línea y las llamadas relacionadas.
# Esto ayuda a encontrar y solucionar problemas.


# PREGUNTA 11:
# ¿Cuándo se ejecuta el bloque finally?
# Respuesta:
# Se ejecuta al finalizar el intento, tanto si ocurre
# un error como si el código funciona correctamente.


# PREGUNTA 12:
# ¿Qué función cumple raise?
# Respuesta:
# Raise permite generar una excepción manualmente.
# En este caso se utiliza cuando el número ingresado
# es menor que 1 o mayor que 10.


# PREGUNTA 13:
# ¿Qué ocurre si el usuario ingresa 5?
# Respuesta:
# El número es válido y no se genera ninguna excepción.
# Se ejecuta finally y el bucle termina porque 5
# está dentro del rango permitido.
# Después se imprime el mensaje de éxito.


# ============================================================
# PARTE 4: CALCULADORA ROBUSTA
# ============================================================

# PREGUNTA 14:
# ¿Cuál es el propósito de break?
# Respuesta:
# Break permite salir del bucle while True cuando
# el cálculo se realiza correctamente.
# Así el programa deja de pedir datos.


# PREGUNTA 15:
# ¿Qué pasa si n2 = 0 y op = '/'?
# Respuesta:
# No se imprime el resultado porque al intentar dividir
# entre cero se genera ZeroDivisionError.
# El programa pasa al bloque except correspondiente,
# muestra el mensaje de error, ejecuta finally
# y vuelve a pedir los datos.


# PREGUNTA 16:
# ¿Qué pasaría si quitamos while True?
# Respuesta:
# El programa solamente permitiría un intento.
# Si el usuario comete un error tendría que ejecutar
# nuevamente el programa para realizar otro cálculo.
# Con while True puede intentar hasta obtener
# un resultado correcto.