from behave import given, when, then
from protocolo import Protocolo

@given('que los dispositivos "{dispositivo1}" y "{dispositivo2}" están autenticados')
def step_impl(context, dispositivo1, dispositivo2):
    context.protocolo = Protocolo()
    context.protocolo.autenticar_dispositivos(dispositivo1, dispositivo2)

@given('que el dispositivo "{dispositivo}" no está autenticado')
def step_impl(context, dispositivo):
    context.protocolo = Protocolo()

@when('el dispositivo "{dispositivo}" envía el mensaje "{mensaje}" al dispositivo "{destino}"')
def step_impl(context, dispositivo, mensaje, destino):
    context.resultado = context.protocolo.enviar_mensaje(dispositivo, mensaje, destino)

@then('el dispositivo "{dispositivo}" debe recibir el mensaje "{mensaje}" correctamente')
def step_impl(context, dispositivo, mensaje):
    assert context.resultado == mensaje, f"Se esperaba {mensaje}, pero se recibió {context.resultado}"

@then('el protocolo debe rechazar la comunicación')
def step_impl(context):
    assert context.resultado == "Error: Autenticación fallida", "La comunicación no fue rechazada como se esperaba"

@then('el protocolo debe retransmitir el mensaje')
def step_impl(context):
    assert context.resultado == "Retransmitido", "El mensaje no fue retransmitido correctamente"
