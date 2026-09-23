
"""
TODO
Crea un programa interactivo que evalúe si una persona mayor de edad está en
condiciones de conducir. Usa como referencia lo visto en la M3 Tarea de Sentencias.
Requisitos:
Entrada de datos: Solicita la edad del usuario y al menos 2 o 3 condiciones
 adicionales.
Sentencias de control: Usa estructuras condicionales (if, else if, else)
 y operadores lógicos (AND, OR, NOT) para evaluar la combinación de datos.
Salida clara: Muestra un mensaje personalizado indicando si la persona puede
 conducir o si debe entregar las llaves inmediatamente.
¡Usa tu creatividad! 
 Piensa en situaciones cómicas o extremas de la vida real.
   ¿Qué imprudencia o descuido no le permitirías a tu abuela antes de subirse al auto?
     (Ejemplo: "¿Olvidó los lentes en la cocina?")
"""
print("Evaluador de conducción 🚗")

edad = int(input("¿Cuántos años tienes? "))

tiene_licencia = input("¿Tienes licencia de conducir? (si/no): ").lower() == "si"
tiene_lentes = input("¿Tienes tus lentes si los necesitas? (si/no): ").lower() == "si"
tiene_sueno = input("¿Tienes mucho sueño? (si/no): ").lower() == "si"

if edad >= 18 and tiene_licencia and tiene_lentes and not tiene_sueno:
    print("✅ Puedes conducir. ¡Maneja con cuidado!")

elif edad < 18 or not tiene_licencia:
    print("❌ No puedes conducir. ¡Entrega las llaves inmediatamente!")

else:
    print("⚠️ Mejor no conduzcas ahora. ¡Abuela, devuelve las llaves!")