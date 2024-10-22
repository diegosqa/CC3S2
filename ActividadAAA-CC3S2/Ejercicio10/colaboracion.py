class DocumentoColaborativo:
    def __init__(self):
        self.contenido = "Hola"
        self.usuarios = []
    
    def abrir_documento(self, usuario):
        self.usuarios.append(usuario)
    
    def editar_texto(self, usuario, original, nuevo):
        # Lógica simplificada que agrega el nuevo texto si coincide el original
        if original in self.contenido:
            self.contenido = self.contenido.replace(original, original + " " + nuevo)

    def obtener_contenido(self):
        return self.contenido

