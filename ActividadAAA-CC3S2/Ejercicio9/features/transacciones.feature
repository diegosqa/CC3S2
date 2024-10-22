Feature: Gestión de transacciones en la base de datos

  Scenario: Transacción exitosa
    Given una transacción comienza
    When realizo una operación de inserción de datos válida
    And confirmo la transacción
    Then los datos deben estar presentes en la base de datos

  Scenario: Transacción fallida con rollback
    Given una transacción comienza
    When realizo una operación de inserción de datos inválida
    And cancelo la transacción
    Then los datos no deben estar presentes en la base de datos

  Scenario: Fallo durante la transacción
    Given una transacción comienza
    When realizo una operación de inserción de datos válida
    And ocurre un fallo antes de confirmar la transacción
    Then los datos no deben estar presentes en la base de datos
