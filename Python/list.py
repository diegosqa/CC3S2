# 1. Crear una lista
colores = ["rojo", "verde", "azul"]
numeros = [1, 2, 3, 4, 5]
mixta = [1, "hola", True]

# 2. Acceder a elementos
print(colores[0])  # Output: rojo
print(colores[-1])  # Output: azul

# 3. Modificar elementos
colores[1] = "amarillo"
print(colores)  # Output: ['rojo', 'amarillo', 'azul']

# 4. Agregar elementos
colores.append("morado")  # Agrega 'morado'
colores.insert(1, "naranja")  # Inserta 'naranja' en la posición 1
colores.extend(["rosa", "blanco"])  # Agrega múltiples elementos
print(colores)

# 5. Eliminar elementos
colores.remove("naranja")  # Elimina 'naranja'
colores.pop()  # Elimina el último elemento
del colores[0]  # Elimina el primer elemento
print(colores)

# 6. Recorrer una lista
for color in colores:
    print(color)

# 7. Rebanado (slicing)
numeros = [0, 1, 2, 3, 4, 5]
print(numeros[1:4])  # Output: [1, 2, 3]

# 8. Funciones útiles
print(len(numeros))  # Output: 6
print(max(numeros))  # Output: 5
print(min(numeros))  # Output: 0
print(sum(numeros))  # Output: 15

# 9. Ordenar y revertir
numeros.sort()
print(numeros)  # Output: [0, 1, 2, 3, 4, 5]
numeros.reverse()
print(numeros)  # Output: [5, 4, 3, 2, 1, 0]

# 10. Listas anidadas
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Acceder a elementos de una lista anidada
print(matriz[0])      # Output: [1, 2, 3] (primera fila de la matriz)
print(matriz[0][1])   # Output: 2 (elemento en la primera fila, segunda columna)

