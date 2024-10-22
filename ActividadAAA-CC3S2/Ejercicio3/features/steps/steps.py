from busqueda_algoritmos import seleccionar_algoritmo

# Paso genérico para manejar diferentes colecciones de datos
@given('la colección de datos contiene {datos}')
def step_impl(context, datos):
    if datos == "una lista ordenada de 1000 elementos":
        context.datos = list(range(1, 1001))  # Genera una lista ordenada de 1 a 1000
    else:
        context.datos = eval(datos)  # Convierte la cadena en una lista de Python

# Paso para una colección vacía
@given('la colección de datos está vacía')
def step_impl(context):
    context.datos = []

# Paso para buscar un número
@when('busco el número {objetivo}')
def step_impl(context, objetivo):
    context.objetivo = int(objetivo)  # Convierte el objetivo en un número entero
    context.algoritmo, context.resultado = seleccionar_algoritmo(context.datos, context.objetivo)

# Paso para verificar el algoritmo utilizado
@then('el algoritmo de búsqueda utilizado debe ser "{algoritmo}"')
def step_impl(context, algoritmo):
    assert context.algoritmo == algoritmo, f"Se esperaba {algoritmo}, pero se utilizó {context.algoritmo}"

# Paso para verificar el índice del resultado
@then('el resultado de la búsqueda debe ser el índice {indice}')
def step_impl(context, indice):
    assert context.resultado == int(indice), f"Se esperaba el índice {indice}, pero se obtuvo {context.resultado}"

# Paso para búsquedas fallidas
@then('no debe encontrarse el número')
def step_impl(context):
    assert context.resultado is None, f"Se esperaba que no se encontrara el número, pero se encontró en {context.resultado}"

# **Corrección aquí**
@then('el algoritmo utilizado debe ser "{algoritmo}"')
def step_impl(context, algoritmo):
    assert context.algoritmo == algoritmo, f"Se esperaba {algoritmo}, pero se utilizó {context.algoritmo}"

