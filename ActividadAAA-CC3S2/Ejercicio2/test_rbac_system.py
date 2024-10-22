import pytest
from rbac_system import Usuario, RBACSystem

def test_admin_puede_editar():
    # Arrange
    usuario = Usuario('administrador')
    sistema = RBACSystem()

    # Act
    resultado = sistema.puede_realizar(usuario, 'editar')

    # Assert
    assert resultado is True

def test_lector_no_puede_editar():
    # Arrange
    usuario = Usuario('lector')
    sistema = RBACSystem()

    # Act
    resultado = sistema.puede_realizar(usuario, 'editar')

    # Assert
    assert resultado is False

def test_editor_puede_ver():
    # Arrange
    usuario = Usuario('editor')
    sistema = RBACSystem()

    # Act
    resultado = sistema.puede_realizar(usuario, 'ver')

    # Assert
    assert resultado is True

def test_editor_no_puede_eliminar():
    # Arrange
    usuario = Usuario('editor')
    sistema = RBACSystem()

    # Act
    resultado = sistema.puede_realizar(usuario, 'eliminar')

    # Assert
    assert resultado is False
