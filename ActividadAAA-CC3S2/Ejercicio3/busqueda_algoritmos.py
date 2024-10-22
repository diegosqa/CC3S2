def busqueda_lineal(datos, objetivo):
    for i, valor in enumerate(datos):
        if valor == objetivo:
            return i
    return None

def busqueda_binaria(datos, objetivo):
    izquierda, derecha = 0, len(datos) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if datos[medio] == objetivo:
            return medio
        elif datos[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return None

def seleccionar_algoritmo(datos, objetivo):
    if not datos:
        return "ninguno", None
    if len(datos) < 10:
        return "búsqueda lineal", busqueda_lineal(datos, objetivo)
    if sorted(datos) == datos:
        return "búsqueda binaria", busqueda_binaria(datos, objetivo)
    return "búsqueda lineal", busqueda_lineal(datos, objetivo)
