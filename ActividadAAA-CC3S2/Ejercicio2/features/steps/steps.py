from behave import given, when, then
from rbac_system import RBACSystem, Usuario

@given('el usuario tiene el rol de "{rol}"')
def step_impl(context, rol):
    context.usuario = Usuario(rol)

@when('intenta realizar la acción "{accion}"')
def step_impl(context, accion):
    context.resultado = RBACSystem().puede_realizar(context.usuario, accion)

@then('la acción debe ser permitida')
def step_impl(context):
    assert context.resultado is True

@then('la acción debe ser denegada')
def step_impl(context):
    assert context.resultado is False
