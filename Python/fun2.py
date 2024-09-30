# 1. Crear una función básica
def saludar():
    print("¡Hola, mundo!")

saludar()  # Llamada a la función

# 2. Función con parámetros
def saludar(nombre):
    print(f"¡Hola, {nombre}!")

saludar("Carlos")  # Output: ¡Hola, Carlos!

# 3. Función con valor de retorno
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(resultado)  # Output: 8

# 4. Función con parámetros por defecto
def saludar(nombre="Mundo"):
    print(f"¡Hola, {nombre}!")

saludar()  # Output: ¡Hola, Mundo!
saludar("Ana")  # Output: ¡Hola, Ana!

# 5. Función con múltiples parámetros
def calcular(a, b, operacion="sumar"):
    if operacion == "sumar":
        return a + b
    elif operacion == "multiplicar":
        return a * b

print(calcular(3, 4))  # Output: 7
print(calcular(3, 4, operacion="multiplicar"))  # Output: 12

# 6. Uso de *args
def sumar_todos(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(sumar_todos(1, 2, 3, 4, 5))  # Output: 15

# 7. Uso de **kwargs
def mostrar_info(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Carlos", edad=30, ciudad="Lima")

# 8. Variables locales y alcance
def funcion():
    x = 10  # Esta variable tiene un alcance local
    print(x)

funcion()

# 9. Funciones como objetos
def saludar():
    return "¡Hola!"

mensaje = saludar  # Asignamos la función a una variable
print(mensaje())   # Output: ¡Hola!
