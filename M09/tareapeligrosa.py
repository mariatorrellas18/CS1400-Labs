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
