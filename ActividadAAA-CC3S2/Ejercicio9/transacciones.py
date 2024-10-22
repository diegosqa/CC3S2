import sqlite3

class BaseDeDatos:
    def __init__(self):
        self.conexion = sqlite3.connect(":memory:")
        self.cursor = self.conexion.cursor()
        self.cursor.execute("CREATE TABLE tabla (columna TEXT)")
        self.transaccion_activa = False

    def comenzar_transaccion(self):
        self.transaccion_activa = True

    def insertar(self, query):
        if self.transaccion_activa:
            try:
                self.cursor.execute(query)
                return "Operación exitosa"
            except sqlite3.Error as e:
                return f"Error: {e}"
        else:
            return "No hay transacción activa"

    def confirmar(self):
        if self.transaccion_activa:
            self.conexion.commit()
            self.transaccion_activa = False
            return "Transacción confirmada"

    def rollback(self):
        if self.transaccion_activa:
            self.conexion.rollback()
            self.transaccion_activa = False
            return "Transacción cancelada"

    def fallo(self):
        if self.transaccion_activa:
            self.transaccion_activa = False
            return "Error: Fallo del sistema"

    def consultar(self, query):
        try:
            self.cursor.execute(query)
            return self.cursor.fetchone()
        except sqlite3.Error:
            return None

