from behave import given, when, then
from train_model import ModeloML

@given('tengo un conjunto de datos de entrenamiento')
def step_impl(context):
    context.modelo = ModeloML()
    context.X_train, context.X_test, context.y_train, context.y_test = context.modelo.cargar_datos()

@when('entreno el modelo de machine learning')
def step_impl(context):
    context.modelo.entrenar_modelo(context.X_train, context.y_train)

@then('las métricas de desempeño deben ser precisas, incluyendo una precisión de al menos 0.90')
def step_impl(context):
    accuracy, f1 = context.modelo.evaluar_modelo(context.X_test, context.y_test)
    assert accuracy >= 0.90, f"Precisión esperada >= 0.90, pero fue {accuracy}"

@given('tengo un conjunto de datos de prueba')
def step_impl(context):
    # Usamos los mismos datos cargados anteriormente
    pass

@when('valido el modelo entrenado')
def step_impl(context):
    # El modelo ya está entrenado en los pasos anteriores
    pass

@then('las métricas de validación deben ser superiores a 0.85 para F1-score')
def step_impl(context):
    accuracy, f1 = context.modelo.evaluar_modelo(context.X_test, context.y_test)
    assert f1 >= 0.85, f"F1-score esperado >= 0.85, pero fue {f1}"

