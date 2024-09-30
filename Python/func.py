# 1. Crear una función básica
def saludar():
    print("Hola, mundo!")

saludar()  # Llama a la función

# 2. Función con parámetros
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Ana")  # Llama a la función con el argumento "Ana"

# 3. Función con valor de retorno
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(resultado)  # Output: 8

# 4. Función con parámetros por defecto
def saludar(nombre="Mundo"):
    print(f"Hola, {nombre}!")

saludar()         # Usa el valor por defecto: Mundo
saludar("Carlos")  # Usa el argumento: Carlos

# 5. Función con múltiples parámetros
def multiplicar(a, b, c):
    return a * b * c

resultado = multiplicar(2, 3, 4)
print(resultado)  # Output: 24

# 6. Uso de *args para múltiples argumentos
def sumar_todos(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

resultado = sumar_todos(1, 2, 3, 4, 5)
print(resultado)  # Output: 15

# 7. Uso de **kwargs para argumentos nombrados
def mostrar_info(**info):
    for clave, valor in info.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Carlos", edad=25, ciudad="Lima")

# 8. Variables locales y alcance
def funcion():
    x = 10  # Esta variable tiene un alcance local
    print(x)

funcion()

# 9. Funciones como objetos
def saludar():
    return "Hola!"

mensaje = saludar  # Asignamos la función a una variable
print(mensaje())   # Llamamos la función a través de la variable
