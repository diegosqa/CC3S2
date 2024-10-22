import pytest
from compilador import Compilador, ErrorLexico, ErrorSintactico

def test_codigo_valido():
    # Arrange
    compilador = Compilador()
    codigo = "print(5 + 3)"
    
    # Act
    resultado = compilador.compilar_y_ejecutar(codigo)
    
    # Assert
    assert resultado == 8

def test_error_lexico():
    # Arrange
    compilador = Compilador()
    codigo = "print(5 + *)"
    
    # Act and Assert
    with pytest.raises(ErrorLexico):
        compilador.compilar_y_ejecutar(codigo)

def test_error_sintactico():
    # Arrange
    compilador = Compilador()
    codigo = "print(5 + 3"
    
    # Act and Assert
    with pytest.raises(ErrorSintactico):
        compilador.compilar_y_ejecutar(codigo)

