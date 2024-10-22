Feature: Sincronización de datos en una aplicación multihilo

  Scenario: Evitar condiciones de carrera en el acceso a un recurso compartido
    Given un contador inicializado en 0
    When varios hilos incrementan el contador 100 veces cada uno
    Then el valor final del contador debe ser 1000
    And no deben ocurrir inconsistencias en el acceso al recurso compartido

  Scenario: Sincronización de acceso concurrente utilizando locks
    Given un recurso compartido inicializado en 0
    When varios hilos acceden al recurso y lo modifican
    Then no deben ocurrir condiciones de carrera
    And el resultado final debe ser correcto
