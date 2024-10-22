Feature: Sistema de búsqueda eficiente

  Scenario: Realizar una búsqueda en una pequeña colección de datos
    Given la colección de datos contiene [1, 2, 3, 4, 5]
    When busco el número 3
    Then el algoritmo de búsqueda utilizado debe ser "búsqueda lineal"
    And el resultado de la búsqueda debe ser el índice 2

  Scenario: Realizar una búsqueda en una gran colección de datos ordenados
    Given la colección de datos contiene una lista ordenada de 1000 elementos
    When busco el número 500
    Then el algoritmo de búsqueda utilizado debe ser "búsqueda binaria"
    And el resultado de la búsqueda debe ser el índice 499

  Scenario: Realizar una búsqueda en una colección vacía
    Given la colección de datos está vacía
    When busco el número 10
    Then no debe encontrarse el número
    And el algoritmo utilizado debe ser "ninguno"
