from train_model import ModeloML

def test_entrenamiento_y_validacion():
    # Arrange
    modelo = ModeloML()
    X_train, X_test, y_train, y_test = modelo.cargar_datos()

    # Act
    modelo.entrenar_modelo(X_train, y_train)
    accuracy, f1 = modelo.evaluar_modelo(X_test, y_test)

    # Assert
    assert accuracy >= 0.90, f"Precisión esperada >= 0.90, pero fue {accuracy}"
    assert f1 >= 0.85, f"F1-score esperado >= 0.85, pero fue {f1}"

