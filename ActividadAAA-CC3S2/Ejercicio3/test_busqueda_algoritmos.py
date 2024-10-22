import pytest
from busqueda_algoritmos import busqueda_lineal, busqueda_binaria, seleccionar_algoritmo

def test_busqueda_lineal():
    datos = [1, 2, 3, 4, 5]
    resultado = busqueda_lineal(datos, 3)
    assert resultado == 2

def test_busqueda_binaria():
    datos = list(range(1, 1001))  # Lista de 1 a 1000
    resultado = busqueda_binaria(datos, 500)
    assert resultado == 499

def test_seleccionar_algoritmo_lineal():
    datos = [5, 1, 3, 2, 4]
    algoritmo, resultado = seleccionar_algoritmo(datos, 3)
    assert algoritmo == "búsqueda lineal"
    assert resultado == 2

def test_seleccionar_algoritmo_binario():
    datos = list(range(1, 1001))  # Lista de 1 a 1000
    algoritmo, resultado = seleccionar_algoritmo(datos, 500)
    assert algoritmo == "búsqueda binaria"
    assert resultado == 499

def test_busqueda_en_lista_vacia():
    datos = []
    algoritmo, resultado = seleccionar_algoritmo(datos, 10)
    assert algoritmo == "ninguno"
    assert resultado is None

