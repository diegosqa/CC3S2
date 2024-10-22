import pytest
from colaboracion import DocumentoColaborativo

def test_edicion_con_dos_usuarios():
    # Arrange
    doc = DocumentoColaborativo()
    doc.abrir_documento('Alice')
    doc.abrir_documento('Bob')

    # Act
    doc.editar_texto('Alice', 'Hola', 'Hola Mundo')
    doc.editar_texto('Bob', 'Hola', 'Hola a todos')

    # Assert
    assert doc.obtener_contenido() == "Hola a todos Mundo"

