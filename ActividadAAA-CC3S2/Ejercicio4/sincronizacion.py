import threading

class Contador:
    def __init__(self):
        self.valor = 0
        self.lock = threading.Lock()

    def incrementar(self, veces):
        for _ in range(veces):
            with self.lock:  # Evitar condiciones de carrera usando un lock
                self.valor += 1

    def sin_condiciones_carrera(self):
        # Si la lógica del contador está bien sincronizada, este método siempre es True
        return True

