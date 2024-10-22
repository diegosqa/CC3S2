from behave import given, when, then
import threading
from sincronizacion import Contador

# Paso para inicializar el contador
@given('un contador inicializado en 0')
def step_impl(context):
    context.contador = Contador()

# Paso para incrementar el contador desde varios hilos
@when('varios hilos incrementan el contador {veces} veces cada uno')
def step_impl(context, veces):
    threads = []
    for _ in range(10):
        thread = threading.Thread(target=context.contador.incrementar, args=(int(veces),))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

# Paso para verificar el valor final del contador
@then('el valor final del contador debe ser {valor_final}')
def step_impl(context, valor_final):
    assert context.contador.valor == int(valor_final), f"Se esperaba {valor_final}, pero se obtuvo {context.contador.valor}"

# Paso para verificar que no ocurrieron condiciones de carrera
@then('no deben ocurrir inconsistencias en el acceso al recurso compartido')
def step_impl(context):
    # El test de concurrencia garantiza que no haya condiciones de carrera
    assert context.contador.sin_condiciones_carrera(), "Hubo una condición de carrera."


