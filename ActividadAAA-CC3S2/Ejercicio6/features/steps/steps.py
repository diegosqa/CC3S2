from behave import given, when, then
from cache import Cache

@given('el cache tiene capacidad {capacidad:d}')
def step_impl(context, capacidad):
    context.cache = Cache(capacidad)

@given('la política de reemplazo es "{politica}"')
def step_impl(context, politica):
    context.cache.set_policy(politica)

@when('agrego los datos "{datos}"')
def step_impl(context, datos):
    # Corregir el manejo de las comillas y separar correctamente
    datos = datos.replace('"', '').split(", ")
    for dato in datos:
        context.cache.add(dato)

@when('agrego el dato "{dato}"')
def step_impl(context, dato):
    context.cache.add(dato)

@when('accedo al dato "{dato}"')
def step_impl(context, dato):
    context.cache.get(dato)

@then('los datos en el cache deben ser {esperado}')
def step_impl(context, esperado):
    esperado = eval(esperado)  # Convertir string en una lista
    assert context.cache.items() == esperado, f"Se esperaba {esperado}, pero se obtuvo {context.cache.items()}"

@then('el dato "{dato}" debe ser reemplazado y el cache debe ser {esperado}')
def step_impl(context, dato, esperado):
    esperado = eval(esperado)
    assert context.cache.items() == esperado, f"Se esperaba {esperado}, pero se obtuvo {context.cache.items()}"

