Feature: Colaboración en tiempo real para la edición de documentos

  Scenario: Múltiples usuarios editando el mismo documento
    Given el documento está abierto por el usuario "Alice"
    And el usuario "Bob" también abre el documento
    When Alice edita el texto "Hola" a "Hola Mundo"
    And Bob edita el texto "Hola" a "Hola a todos"
    Then el documento debe mostrar "Hola a todos Mundo" en ambos usuarios

  Scenario: Sincronización en tiempo real de cambios
    Given el usuario "Alice" está editando el documento
    And el usuario "Bob" está viendo el documento
    When Alice agrega el texto "Nuevo texto"
    Then Bob debe ver el texto "Nuevo texto" inmediatamente

  Scenario: Resolución de conflictos en tiempo real
    Given Alice y Bob están editando el mismo documento
    When Alice y Bob hacen cambios simultáneos en la misma línea
    Then el sistema debe resolver el conflicto sin pérdida de datos

