Feature: Sistema de cache con políticas de reemplazo

  Scenario: Acceder a los datos utilizando la política FIFO
    Given el cache tiene capacidad 3
    And la política de reemplazo es "FIFO"
    When agrego los datos "A", "B" y "C"
    Then los datos en el cache deben ser ["A", "B", "C"]
    When agrego el dato "D"
    Then el dato "A" debe ser reemplazado y el cache debe ser ["B", "C", "D"]

  Scenario: Acceder a los datos utilizando la política LRU
    Given el cache tiene capacidad 3
    And la política de reemplazo es "LRU"
    When agrego los datos "A", "B" y "C"
    Then los datos en el cache deben ser ["A", "B", "C"]
    When accedo al dato "A" y luego agrego el dato "D"
    Then el dato "B" debe ser reemplazado y el cache debe ser ["A", "C", "D"]

