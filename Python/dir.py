# 1. Crear un diccionario
persona = {
    "nombre": "Carlos",
    "edad": 30,
    "ciudad": "Lima"
}

# 2. Acceder a valores
print(persona["nombre"])  # Output: Carlos
print(persona["edad"])    # Output: 30

# 3. Modificar un valor
persona["edad"] = 31
print(persona["edad"])  # Output: 31

# 4. Agregar un nuevo par clave-valor
persona["profesión"] = "Ingeniero"
print(persona)  # Output: {'nombre': 'Carlos', 'edad': 31, 'ciudad': 'Lima', 'profesión': 'Ingeniero'}

# 5. Eliminar elementos
persona.pop("ciudad")  # Elimina la clave 'ciudad'
print(persona)  # Output: {'nombre': 'Carlos', 'edad': 31, 'profesión': 'Ingeniero'}

del persona["edad"]  # Elimina la clave 'edad'
print(persona)  # Output: {'nombre': 'Carlos', 'profesión': 'Ingeniero'}

# 6. Recorrer el diccionario
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# 7. Métodos útiles
print(persona.keys())   # Output: dict_keys(['nombre', 'profesión'])
print(persona.values()) # Output: dict_values(['Carlos', 'Ingeniero'])
print(persona.items())  # Output: dict_items([('nombre', 'Carlos'), ('profesión', 'Ingeniero')])

# 8. Diccionarios anidados
estudiantes = {
    "Carlos": {"edad": 25, "carrera": "Ingeniería"},
    "Ana": {"edad": 22, "carrera": "Medicina"}
}

print(estudiantes["Carlos"]["edad"])  # Output: 25
print(estudiantes["Ana"]["carrera"])  # Output: Medicina

# 9. Verificar si una clave existe
if "nombre" in persona:
    print("La clave 'nombre' existe en el diccionario.")
