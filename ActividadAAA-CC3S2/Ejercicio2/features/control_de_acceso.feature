Feature: Sistema de control de acceso basado en roles (RBAC)

  Scenario: Acceso permitido para administrador
    Given el usuario tiene el rol de "administrador"
    When intenta realizar la acción "editar"
    Then la acción debe ser permitida

  Scenario: Acceso denegado para lector
    Given el usuario tiene el rol de "lector"
    When intenta realizar la acción "editar"
    Then la acción debe ser denegada

  Scenario: Acceso permitido para editor
    Given el usuario tiene el rol de "editor"
    When intenta realizar la acción "ver"
    Then la acción debe ser permitida

  Scenario: Acceso denegado para editor
    Given el usuario tiene el rol de "editor"
    When intenta realizar la acción "eliminar"
    Then la acción debe ser denegada
