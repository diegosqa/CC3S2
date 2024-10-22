from gestion_tareas import GestionTareas
from behave import given, when, then
import pytest


@given('el sistema de gestión de tareas está vacío')
def step_impl(context):
    context.gestion_tareas = GestionTareas()  # Inicializamos la gestión de tareas


@when('agrego la tarea "{tarea}" con prioridad {prioridad:d}')
def step_impl(context, tarea, prioridad):
    context.gestion_tareas.agregar_tarea(tarea, prioridad)


@when('intento procesar una tarea')
def step_impl(context):
    try:
        context.tarea_procesada = context.gestion_tareas.procesar_tarea()
    except Exception as e:
        context.error = str(e)


@then('la tarea "{tarea}" debe ser procesada primero')
def step_impl(context, tarea):
    tarea_procesada = context.gestion_tareas.procesar_tarea()
    assert tarea_procesada == tarea, f'Se esperaba {tarea}, pero se procesó {tarea_procesada}'


@then('la tarea "{tarea}" debe ser procesada después')
def step_impl(context, tarea):
    tarea_procesada = context.gestion_tareas.procesar_tarea()
    assert tarea_procesada == tarea, f'Se esperaba {tarea}, pero se procesó {tarea_procesada}'


@then('la tarea "{tarea}" debe ser procesada al final')
def step_impl(context, tarea):
    tarea_procesada = context.gestion_tareas.procesar_tarea()
    assert tarea_procesada == tarea, f'Se esperaba {tarea}, pero se procesó {tarea_procesada}'


@then('se debe lanzar una excepción indicando "No hay tareas para procesar"')
def step_impl(context):
    assert hasattr(context, 'error'), 'No se lanzó ninguna excepción'
    assert context.error == "No hay tareas para procesar", f'Se esperaba "No hay tareas para procesar", pero se recibió "{context.error}"'

