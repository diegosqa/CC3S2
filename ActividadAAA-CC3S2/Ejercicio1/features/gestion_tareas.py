import heapq

class GestionTareas:
    def __init__(self):
        self.tareas = []  # Lista para almacenar las tareas como un heap (cola de prioridad)
        self.contador = 0  # Contador para asegurar el orden en caso de tareas con la misma prioridad

    def agregar_tarea(self, tarea, prioridad):
        # Agregamos la tarea a la lista con prioridad negativa (para que heapq lo trate como max-heap)
        heapq.heappush(self.tareas, (-prioridad, self.contador, tarea))
        self.contador += 1

    def procesar_tarea(self):
        if not self.tareas:
            raise Exception("No hay tareas para procesar")
        # Extraemos la tarea de mayor prioridad
        _, _, tarea = heapq.heappop(self.tareas)
        return tarea

