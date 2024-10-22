from cryptography.fernet import Fernet

class Protocolo:
    def __init__(self):
        self.autenticados = set()
        self.clave = Fernet.generate_key()
        self.cifrador = Fernet(self.clave)

    def autenticar_dispositivos(self, dispositivo1, dispositivo2):
        self.autenticados.add(dispositivo1)
        self.autenticados.add(dispositivo2)

    def enviar_mensaje(self, dispositivo, mensaje, destino):
        if dispositivo not in self.autenticados:
            return "Error: Autenticación fallida"
        mensaje_encriptado = self.cifrar_mensaje(mensaje)
        # Simulando que enviamos y recibimos el mensaje correctamente
        return self.descifrar_mensaje(mensaje_encriptado)

    def cifrar_mensaje(self, mensaje):
        return self.cifrador.encrypt(mensaje.encode())

    def descifrar_mensaje(self, mensaje_encriptado):
        return self.cifrador.decrypt(mensaje_encriptado).decode()

    def manejar_perdida(self, mensaje):
        # Simulación de la pérdida de un paquete y retransmisión
        return "Retransmitido"
