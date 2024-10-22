# features/gestion_de_tareas.feature
Feature: Gestión de tareas con prioridades

  Scenario: Procesar tareas en orden de prioridad
    Given el sistema de gestión de tareas está vacío
    When agrego la tarea "Lavar la ropa" con prioridad 1
    And agrego la tarea "Comprar víveres" con prioridad 3
    And agrego la tarea "Estudiar para el examen" con prioridad 2
    Then la tarea "Comprar víveres" debe ser procesada primero
    And la tarea "Estudiar para el examen" debe ser procesada después
    And la tarea "Lavar la ropa" debe ser procesada al final

  Scenario: Intentar procesar una tarea cuando la cola está vacía
    Given el sistema de gestión de tareas está vacío
    When intento procesar una tarea
    Then se debe lanzar una excepción indicando "No hay tareas para procesar"

