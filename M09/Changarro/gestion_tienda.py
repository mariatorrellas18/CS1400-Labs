
# gestion_tienda.py

# Este módulo contiene las funciones para gestionar el inventario de la tienda.
# Crear las 3 funciones que se describen a continuación:
# Una para agregar un producto, debe recibir inventario, nombre y precio.
# Esta debe tener un try except ValueError para manejar el error si el precio no es un número.
# Otra para buscar el precio de un producto, debe recibir inventario y nombre. Utiliza .get()
# Y una última función para listar todos los productos, debe recibir el inventario.
# Tener una opcion por si esta vacio el inventario.

# TODO #3 Agregar comenantarios a cada función explicando qué hace y cómo funciona.

def agregar_producto(inventario, nombre, precio):
    """
    Esta función agrega un producto al inventario.
    Recibe el inventario, el nombre y el precio del producto.
    Convierte el precio a float para asegurarse de que sea un número.
    Si el producto ya existe, actualiza su precio.
    Si el precio no es válido, devuelve False usando try/except.
    """
    try:
        # Convertimos a float para asegurar que sea un número
        precio_num = float(precio)
        inventario[nombre] = precio_num
        return True
    except ValueError:
        # Si no se puede convertir a número, devolvemos False
        return False

def buscar_precio(inventario, nombre):
    """
    Esta función busca el precio de un producto en el inventario.
    Recibe el diccionario y el nombre del producto.
    Utiliza .get() para buscar el precio.
    Si encuentra el producto, devuelve su precio.
    Si no existe, devuelve None.
    """
    # Usamos .get() para evitar que el programa falle si la llave no existe
    return inventario.get(nombre, None)

def listar_productos(inventario):
    """
    Esta función muestra todos los productos del inventario.
    Primero verifica si el diccionario está vacío.
    Si está vacío, muestra un mensaje al usuario.
    Si tiene productos, utiliza un ciclo for para recorrerlos
    y mostrar el nombre y el precio de cada producto.
    """
    if not inventario:
        print("\n> El inventario está vacío.")
    else:
        print("\n--- Inventario Actual ---")
        for producto, precio in inventario.items():
            print(f"• {producto}: ${precio:.2f}")
