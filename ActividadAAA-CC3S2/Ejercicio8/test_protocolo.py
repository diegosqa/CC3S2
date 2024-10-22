from protocolo import Protocolo

def test_comunicacion_exitosa():
    # Arrange
    protocolo = Protocolo()
    protocolo.autenticar_dispositivos("A", "B")
    mensaje = "Hola"
    
    # Act
    resultado = protocolo.enviar_mensaje("A", mensaje, "B")
    
    # Assert
    assert resultado == mensaje

def test_autenticacion_fallida():
    # Arrange
    protocolo = Protocolo()
    
    # Act
    resultado = protocolo.enviar_mensaje("A", "Hola", "B")
    
    # Assert
    assert resultado == "Error: Autenticación fallida"

def test_retransmision():
    # Arrange
    protocolo = Protocolo()
    
    # Act
    resultado = protocolo.manejar_perdida("Hola")
    
    # Assert
    assert resultado == "Retransmitido"
