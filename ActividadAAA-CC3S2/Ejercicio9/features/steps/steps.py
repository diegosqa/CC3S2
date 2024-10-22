from behave import given, when, then
from transacciones import BaseDeDatos

@given('una transacción comienza')
def step_impl(context):
    context.db = BaseDeDatos()
    context.db.comenzar_transaccion()

@when('realizo una operación de inserción de datos válida')
def step_impl(context):
    context.resultado = context.db.insertar("INSERT INTO tabla (columna) VALUES ('valor')")

@when('realizo una operación de inserción de datos inválida')
def step_impl(context):
    context.resultado = context.db.insertar("INSERT INTO tabla (columna_invalida) VALUES ('valor')")

@when('confirmo la transacción')
def step_impl(context):
    context.db.confirmar()

@when('cancelo la transacción')
def step_impl(context):
    context.db.rollback()

@when('ocurre un fallo antes de confirmar la transacción')
def step_impl(context):
    context.db.fallo()

@then('los datos deben estar presentes en la base de datos')
def step_impl(context):
    assert context.db.consultar("SELECT * FROM tabla") is not None, "Los datos no fueron insertados correctamente"

@then('los datos no deben estar presentes en la base de datos')
def step_impl(context):
    assert context.db.consultar("SELECT * FROM tabla") is None, "Los datos no fueron eliminados correctamente tras el fallo"
