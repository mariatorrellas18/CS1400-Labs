#Sección 1: Conteo Inverso con range()
#Analizaremos cómo usar pasos negativos para contar hacia atrás.

#Código 1.1:
#Python
# Conteo descendente
num = int(input("Introduce el número inicial:"))

for i in range(num, 0, -1):
    print("Conteo:", i)
#Análisis:
# 1. Ejecuta el programa e introduce 10. Al observar la consola, ¿en qué número comenzó la cuenta y en cuál terminó?
# Inicio: num | Fin: 0

# 2. ¿Por qué es necesario que el parámetro step (paso) sea un número negativo al realizar un conteo descendente?
# Porque en un conteo descendente necesitamos que los números vayan disminuyendo. Por eso el step debe ser negativo, por ejemplo -1, para restar uno en cada repetición.
# 3. ¿Por qué el valor final se configuró en 0 si queríamos que el conteo se detuviera en el número 1?
# Porque el parámetro final en range() es exclusivo, es decir, el conteo se detiene antes de llegar a ese valor. Por eso, para que el conteo incluya el 1, debemos poner 0 como valor final.

#Práctica de Sección:
# 4. Modifica el código para que cuente hacia atrás de 2 en 2, comenzando desde el número elegido por el usuario y deteniéndose exactamente en el 0 (inclusive). Escribe la línea de tu range() modificada:

#Respuesta: range (num , -1 , -2)

#Sección 2: Funciones Matemáticas de Python (math)
#Python incluye funciones matemáticas integradas (built-in) y un módulo especializado llamado math.


##Código 2.1:
#Python
import math

decNum = -34.5678
intNum = 9

print( round(decNum, 2) )   # Línea A
print( round(decNum, 0) )   # Línea B
print( int(decNum) )        # Línea C
print( abs(decNum) )        # Línea D

print( math.pow(intNum, 2) ) # Línea E
print( math.sqrt(intNum) )   # Línea F

#Predicciones de Salida (Escribe el resultado exacto):
#5.¿ Resultado de la Línea A round(decNum, 2)? -34.57

#6. ¿Resultado de la Línea B round(decNum, 0)? -35

#7. ¿ Resultado de la Línea C int(decNum)?  (Pista: ¿Redondea o trunca los decimales?) -34

#8. ¿Resultado de la Línea D abs(decNum)?  34.5678

#9. ¿Resultado de la Línea E math.pow(intNum, 2)?  81.0

#10. ¿Resultado de la Línea F math.sqrt(intNum)?  3.0

##Sección 3: Comparación de Textos mediante ASCII / Unicode
#Las funciones max() y min() en Python no solo funcionan con números; en cadenas de texto comparan valores según la tabla de caracteres ASCII/Unicode.

##Código 3.1:
#Python
miMax = max("Banano", "manzana", "Zanahoria")
print("El máximo es:", miMax)
##Análisis:
#11. Antes de ejecutar: ¿Cuál crees que será el resultado devuelto por max()?

#Predicción: manzana
#12. Ejecuta el código. ¿Cuál fue el resultado real devuelto?

#Resultado: manzana
 

#13. Sabiendo que en la tabla ASCII las mayúsculas tienen valores numéricos menores que las minúsculas, explica por qué "manzana" fue seleccionada como la mayor frente a "Zanahoria".

#14. Cambia la función de max() a min(). ¿Qué valor obtienes ahora y por qué?

#Resultado: Banano

#Sección 4: Aplicación Práctica – Física y Matemáticas
#La policía de tránsito calcula la velocidad v de un auto a partir de la longitud d de la huella de frenado utilizando la fórmula: v = \sqrt{20 \cdot d}.

##Código 4.1:
#Python
import math

d = int(input("Ingresa la longitud de la huella de frenado (en metros): "))

# Completa la ecuación usando math.sqrt():
v = math.sqrt(20 * d)

print("Velocidad estimada del auto:", round(v, 2), "km/h")
#Análisis:
#15. Completa la asignación v = en el código superior utilizando la función math.sqrt() y la fórmula entregada. Escribe la línea completa a continuación:

#Respuesta: v = math.sqrt(20 * d)

##Sección 5: Segmentación de Cadenas (Slicing)
#El slicing o rebanado permite extraer subcadenas utilizando la sintaxis cadena[inicio:fin:paso].

##Código 5.1:
#Python
nombre = "Building Puentes"

print("Índice 0:", nombre[0])
print("Segmento:", nombre[8:15])
##Análisis:
#16. ¿Qué carácter imprime exactamente nombre[0]?
#  B

#17. ¿En qué posición (índice) exacta se encuentra el espacio en blanco entre ambas palabras? 
# 8

#18. Modifica los índices en nombre[X:Y] para extraer e imprimir exactamente la palabra "Puentes".

#Opción con 2 valores: nombre[ 8 : 15 ]

#Opción con límite implícito: nombre[ 8 : ]
print(nombre[8:15])
print(nombre[8:])


##Sección 6: Filtrado e Inspección de Caracteres en Cadenas
#Podemos usar bucles combinados con condicionales para inspeccionar y filtrar tipos específicos de caracteres dentro de un texto.

##Código 6.1:
#Python
texto = input("Ingresa una frase con letras y números: ")
contador_numeros = 0

for caracter in texto:
    if caracter >= "0" and caracter <= "9":
        contador_numeros += 1

print("Total de dígitos numéricos encontrados:", contador_numeros)
##Análisis:
#19. Ejecuta el programa e ingresa el texto "3 tigres en 2 árboles". ¿Qué valor imprime contador_numeros?
#  2
#20. Observa la condición del if. Explica cómo evalúa Python si un carácter individual es un dígito numérico usando los operadores >= y <=.
#  Python compara el carácter con los caracteres "0" y "9" en la tabla ASCII. Si el carácter está entre "0" y "9", se considera un dígito numérico.

##Sección 7: Investigación de Métodos de Cadenas (String Methods)
#Investiga en la documentación oficial de Python o en W3Schools el funcionamiento de los siguientes métodos y explica brevemente para qué sirven:

 #21. Método .rfind('a'):
#Descripción: Devuelve el índice de la última aparición del carácter 'a' en la cadena, o -1 si no se encuentra.

 #22. Método .isalpha():
#Descripción: Devuelve True si todos los caracteres de la cadena son letras del alfabeto y hay al menos un carácter, de lo contrario devuelve False.

 #23. Método .isdigit():
#Descripción: Devuelve True si todos los caracteres de la cadena son dígitos y hay al menos un carácter, de lo contrario devuelve False.

 #24. Método .lower():
#Descripción: Devuelve una copia de la cadena con todos los caracteres en minúsculas.

 #25. Método .upper():
#Descripción: Devuelve una copia de la cadena con todos los caracteres en mayúsculas.