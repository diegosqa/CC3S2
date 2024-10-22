Feature: Entrenamiento y validación del modelo de Machine Learning

  Scenario: Entrenar el modelo y obtener métricas de desempeño
    Given tengo un conjunto de datos de entrenamiento
    When entreno el modelo de machine learning
    Then las métricas de desempeño deben ser precisas, incluyendo una precisión de al menos 0.90

  Scenario: Validar el modelo con datos de prueba
    Given tengo un conjunto de datos de prueba
    When valido el modelo entrenado
    Then las métricas de validación deben ser superiores a 0.85 para F1-score
