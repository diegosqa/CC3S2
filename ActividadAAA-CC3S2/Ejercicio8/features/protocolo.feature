Feature: Protocolo de comunicación seguro

  Scenario: Enviar un mensaje encriptado y autenticado exitosamente
    Given que los dispositivos "A" y "B" están autenticados
    When el dispositivo "A" envía el mensaje "Hola" al dispositivo "B"
    Then el dispositivo "B" debe recibir el mensaje "Hola" correctamente

  Scenario: Intentar enviar un mensaje sin autenticación
    Given que el dispositivo "A" no está autenticado
    When el dispositivo "A" intenta enviar un mensaje
    Then el protocolo debe rechazar la comunicación

  Scenario: Manejar pérdida de paquete
    Given que los dispositivos "A" y "B" están autenticados
    When el dispositivo "A" envía el mensaje "Hola" y se pierde un paquete
    Then el protocolo debe retransmitir el mensaje
