# 1. Condicional básico
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# 2. Uso de operadores lógicos
edad = 25
tiene_identificacion = True

if edad >= 18 and tiene_identificacion:
    print("Puedes entrar al club")
else:
    print("No puedes entrar al club")

# 3. Condicional anidado
edad = 16
con_permiso = True

if edad >= 18:
    print("Puedes manejar")
else:
    if con_permiso:
        print("Puedes manejar con permiso")
    else:
        print("No puedes manejar")

# 4. Uso de elif
nota = 85

if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Aprobado")
else:
    print("Desaprobado")

# 5. Comparación de cadenas de texto
color = "rojo"

if color == "rojo":
    print("El color es rojo")
elif color == "azul":
    print("El color es azul")
else:
    print("Es otro color")

# 6. Operador ternario
edad = 20
mensaje = "Mayor de edad " if edad >= 18 else "Menor de edad"
print(mensaje)  # Output: Mayor de edad

