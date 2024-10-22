# src/task_manager.py
import heapq

class TaskManager:
    def __init__(self):
        self.task_queue = []
        self.task_count = 0

    def add_task(self, task_name, priority):
        """Agrega una tarea con una prioridad específica"""
        self.task_count += 1
        heapq.heappush(self.task_queue, (-priority, self.task_count, task_name))

    def process_task(self):
        """Procesa la siguiente tarea de la cola"""
        if not self.task_queue:
            raise IndexError("No hay tareas para procesar")
        return heapq.heappop(self.task_queue)[2]

