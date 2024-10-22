from behave import given, when, then
from colaboracion import DocumentoColaborativo

@given('el documento está abierto por el usuario "{usuario}"')
def step_impl(context, usuario):
    context.documento = DocumentoColaborativo()
    context.documento.abrir_documento(usuario)

@given('el usuario "{usuario}" también abre el documento')
def step_impl(context, usuario):
    context.documento.abrir_documento(usuario)

@when('Alice edita el texto "{original}" a "{nuevo}"')
def step_impl(context, original, nuevo):
    context.documento.editar_texto('Alice', original, nuevo)

@when('Bob edita el texto "{original}" a "{nuevo}"')
def step_impl(context, original, nuevo):
    context.documento.editar_texto('Bob', original, nuevo)

@then('el documento debe mostrar "{resultado}" en ambos usuarios')
def step_impl(context, resultado):
    assert context.documento.obtener_contenido() == resultado

@then('Bob debe ver el texto "{texto}" inmediatamente')
def step_impl(context, texto):
    assert texto in context.documento.obtener_contenido()

