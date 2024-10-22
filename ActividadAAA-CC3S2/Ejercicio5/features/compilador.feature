Feature: Compilación de un lenguaje de programación básico

  Scenario: Compilar y ejecutar código válido
    Given el código fuente es "print(5 + 3)"
    When se compila y ejecuta el código
    Then la salida debe ser "8"

  Scenario: Manejar errores léxicos
    Given el código fuente es "print(5 + *)"
    When se compila y ejecuta el código
    Then debe lanzarse un error léxico

  Scenario: Manejar errores sintácticos
    Given el código fuente es "print(5 + 3"
    When se compila y ejecuta el código
    Then debe lanzarse un error sintáctico

