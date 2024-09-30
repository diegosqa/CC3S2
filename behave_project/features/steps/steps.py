from behave import Given,Then,When

@given('que tengo el número {numero:d}')
def step_tengo_numero(context, numero):
    if not hasattr(context,'numeros'):
        context.numeros=[]
    context.numeros.append(numero)
@when('los sumo')
def step_sumar_numeros(context):
    context.resultado=sum(context.numeros)

@then('el resultado debe ser {resultado:d}')
def step_verificar_resultado(context,resultado):
    assert context.resultado==resultado, f"Esperaba {resultado}, pero obttuve {context.resultado}"