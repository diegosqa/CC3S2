# 1. Bucle for básico
colores = ["rojo", "azul", "verde"]
for color in colores:
    print(color)

# 2. Bucle for con range()
for i in range(5):  # Imprime números del 0 al 4
    print(i)

# 3. Bucle while básico
contador = 0
while contador < 5:
    print(contador)
    contador += 1  # Incrementa el contador en 1

# 4. Uso de break
for i in range(10):
    if i == 5:
        break  # Detiene el bucle cuando i es 5
    print(i)

# 5. Uso de continue
for i in range(5):
    if i == 2:
        continue  # Salta la impresión cuando i es 2
    print(i)

# 6. Bucle anidado
for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")

# 7. Iterar sobre una cadena
cadena = "Python"
for letra in cadena:
    print(letra)

# 8. Iterar sobre una lista
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)
