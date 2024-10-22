from transacciones import BaseDeDatos

def test_transaccion_exitosa():
    # Arrange
    db = BaseDeDatos()
    db.comenzar_transaccion()
    
    # Act
    resultado = db.insertar("INSERT INTO tabla (columna) VALUES ('valor')")
    db.confirmar()

    # Assert
    assert resultado == "Operación exitosa"
    assert db.consultar("SELECT * FROM tabla") is not None

def test_rollback_transaccion():
    # Arrange
    db = BaseDeDatos()
    db.comenzar_transaccion()
    
    # Act
    resultado = db.insertar("INSERT INTO tabla (columna_invalida) VALUES ('valor')")
    db.rollback()

    # Assert
    assert "Error" in resultado
    assert db.consultar("SELECT * FROM tabla") is None

def test_fallo_transaccion():
    # Arrange
    db = BaseDeDatos()
    db.comenzar_transaccion()
    
    # Act
    resultado = db.insertar("INSERT INTO tabla (columna) VALUES ('valor')")
    db.fallo()

    # Assert
    assert db.consultar("SELECT * FROM tabla") is None
