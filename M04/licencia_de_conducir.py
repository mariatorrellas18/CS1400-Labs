
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
# Fin del programa de evaluación de conducción

#1. **¿Cuántos commits hiciste?**
#   Hice varios commits durante la actividad para guardar los cambios que fui realizando en el proyecto. alrededor de 30 commits.

#2. **¿Qué método te pareció más fácil de usar para guardar y subir tus cambios a GitHub: los comandos en la terminal o la interfaz visual de Visual Studio Code? ¿Por qué?**
#   Me pareció más fácil usar la terminal de Visual Studio Code porque pude seguir los comandos paso a paso y entender mejor qué estaba haciendo Git en cada momento.

#3. **¿Para qué sirve ejecutar el comando `git status` antes de empezar a trabajar y cómo te ayuda a saber qué archivos han sido modificados o están pendientes por guardar?**
#  `git status` sirve para revisar el estado del repositorio. Me permite ver si hay archivos modificados, archivos nuevos o cambios que todavía no han sido agregados o guardados en un commit.

#4. **¿Por qué es fundamental descargar (`git pull`) los cambios más recientes del repositorio de la profesora antes de realizar y subir tus propias modificaciones al proyecto?**
#  Porque así trabajo con la versión más reciente del proyecto y evito tener archivos viejos o crear conflictos con los cambios que ya hizo la profesora.

#5. **En tus propias palabras, ¿cuál es la diferencia entre hacer un fork de un repositorio en GitHub y clonar un repositorio a tu computadora?**
#   Un fork crea una copia del repositorio en mi propia cuenta de GitHub. En cambio, clonar descarga una copia del repositorio a mi computadora para poder trabajar con los archivos localmente.

#6. **¿Por qué es una buena práctica escribir mensajes claros y descriptivos en cada commit en lugar de usar palabras vagas como "cambios" o "listo"?**
#   Porque un mensaje claro ayuda a saber exactamente qué se modificó en ese commit. También facilita revisar el historial del proyecto y encontrar cambios específicos después.

#7. **¿Qué tipos de mensajes agregaste?**
#   Agregué mensajes relacionados con las condiciones del programa, por ejemplo mensajes indicando si la persona puede conducir o si debe entregar las llaves inmediatamente.

#8. **¿Cuál es tu sentencia preferida?**
#  Mi sentencia preferida es `if`, porque permite comprobar una condición y decidir qué debe hacer el programa dependiendo de si esa condición es verdadera.

#9. **¿Cuándo entra el programa a la segunda sentencia de tu tarea?**
# El programa entra a la segunda sentencia, `elif`, cuando la primera condición del `if` no se cumple. En mi programa ocurre, por ejemplo, si la persona es menor de 18 años o no tiene licencia de conducir.

#10. **¿Qué aprendiste del README.md en tu carpeta M04? No olvides los comentarios!**
#   Aprendí que el archivo README.md sirve para explicar el proyecto, sus instrucciones y cómo funciona. También aprendí que los comentarios en el código son importantes porque ayudan a entender qué hace cada parte del programa y hacen que el código sea más fácil de leer.
