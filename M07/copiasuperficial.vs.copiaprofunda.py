# Copia Superficial vs. Copia Profunda
#(Shallow VS Deep Copy)
# Los siguientes pares clave-valor representan la cantidad de animales en un refugio. Practica observando y programando lo siguiente.

#1. ¿Cuántos perros hay en el refugio al principio?

#2. ¿Cuántos perros se están agregando al refugio?

#3. Escribe la línea de código para eliminar 3 gatos del refugio.

#4. Observa el código para agregar los hurones. ¿Cuántos se agregaron?

#5. Escribe el código para agregar 4 serpientes al refugio.

#6. Escribe una sentencia if para imprimir "Lleno" si el número de perros es mayor a 50.

#7. Escribe una sentencia if para imprimir "No Ratones" si "raton" no es una clave en el diccionario animalesRefugiados.

#8. Nota que la variable refugioOriginal es igual a la variable animalesRefugiados. ¿Es esta una copia superficial o profunda?

#9. Escribe el comando para mostrar los animales de refugioOriginal al final del segmento de código. ¿Muestra los animales originales?

#10. Cambia refugioOriginal para que sea una copia profunda (deep copy) de animalesRefugiados (recuerda importar la librería copy). ¿Muestra los animales originales ahora?

#11. ¿Qué diferencia notas entre una copia profunda y una copia superficial?


import copy

animalesRefugiados = {"perro": 49, "gato": 38, "conejo": 14}
refugioOriginal = animalesRefugiados
animalesRefugiados['perro'] += 2
animalesRefugiados["huron"] = 2
print(animalesRefugiados)