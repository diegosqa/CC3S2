# 1. VARIABLES: Guardar datos en variables
nombre = "Carlos"  # Variable de tipo cadena
edad = 25          # Variable de tipo entero
altura = 1.75      # Variable de tipo flotante
es_estudiante = True  # Variable de tipo booleano

print(f"Hola, mi nombre es {nombre}, tengo {edad} años. ¿Soy estudiante? {es_estudiante}")

# 2. REGLAS PARA NOMBRAR VARIABLES
mi_nombre = "Ana"
edad_actual = 30
altura1 = 1.80
# 1edad = 20  # No es válido porque empieza con un número
# if = 10     # No es válido porque "if" es una palabra reservada

# 3. OPERACIONES CON VARIABLES

# Operaciones aritméticas
a = 10
b = 5
suma = a + b         # Resultado: 15
resta = a - b        # Resultado: 5
producto = a * b     # Resultado: 50
division = a / b     # Resultado: 2.0
potencia = a ** 2    # Resultado: 100

print(f"Suma: {suma}, Resta: {resta}, Producto: {producto}, División: {division}, Potencia: {potencia}")

# Concatenación de cadenas
nombre = "Carlos"
apellido = "García"
nombre_completo = nombre + " " + apellido
print(f"Nombre completo: {nombre_completo}")

# 4. ASIGNACIÓN MÚLTIPLE
x, y, z = 10, 20, 30
print(f"x: {x}, y: {y}, z: {z}")

# 5. CAMBIO DE TIPO DE VARIABLE
x = 5        # x es un entero
x = "cinco"  # Ahora x es una cadena de texto
print(f"x ahora es: {x}")

# 6. ENTRADA DEL USUARIO
nombre_usuario = input("¿Cuál es tu nombre? ")
print("Hola, " + nombre_usuario)

edad_usuario = int(input("¿Cuántos años tienes? "))  # Convertir a entero
print(f"Tienes {edad_usuario} años")

# 7. CONVERSIÓN DE TIPOS (CASTING)
num_str = "25"
num_int = int(num_str)  # Convertir de cadena a entero

print(f"El tipo de num_str es: {type(num_str)}")  # Output: <class 'str'>
print(f"El tipo de num_int es: {type(num_int)}")  # Output: <class 'int'>
