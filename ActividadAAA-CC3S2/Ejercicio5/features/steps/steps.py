from behave import given, when, then
from compilador import Compilador, ErrorLexico, ErrorSintactico

@given('el código fuente es "{codigo}"')
def step_impl(context, codigo):
    context.codigo = codigo
    context.compilador = Compilador()

@when('se compila y ejecuta el código')
def step_impl(context):
    try:
        context.resultado = context.compilador.compilar_y_ejecutar(context.codigo)
        context.error = None
    except (ErrorLexico, ErrorSintactico) as e:
        context.error = str(e)

@then('la salida debe ser "{salida}"')
def step_impl(context, salida):
    assert str(context.resultado) == salida, f"Se esperaba {salida}, pero se obtuvo {context.resultado}"

@then('debe lanzarse un error léxico')
def step_impl(context):
    assert isinstance(context.error, str), "No se lanzó ningún error"
    assert "Error léxico" in context.error, f"Se esperaba un error léxico, pero se obtuvo {context.error}"

@then('debe lanzarse un error sintáctico')
def step_impl(context):
    assert isinstance(context.error, str), "No se lanzó ningún error"
    assert "Error sintáctico" in context.error, f"Se esperaba un error sintáctico, pero se obtuvo {context.error}"

