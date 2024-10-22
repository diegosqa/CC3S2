# tests/test_task_manager.py
import pytest
from src.task_manager import TaskManager

def test_agregar_y_procesar_tareas():
    # Arrange
    manager = TaskManager()
    manager.add_task("Lavar la ropa", 1)  # Prioridad baja
    manager.add_task("Comprar víveres", 3)  # Prioridad alta
    manager.add_task("Estudiar para el examen", 2)  # Prioridad media

    # Act
    first_task = manager.process_task()
    second_task = manager.process_task()
    third_task = manager.process_task()

    # Assert
    assert first_task == "Comprar víveres"
    assert second_task == "Estudiar para el examen"
    assert third_task == "Lavar la ropa"

def test_procesar_cola_vacia():
    # Arrange
    manager = TaskManager()

    # Act & Assert
    with pytest.raises(IndexError, match="No hay tareas para procesar"):
        manager.process_task()

