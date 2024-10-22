from collections import deque

class Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []
        self.policy = 'FIFO'
        self.order = deque()  # Usado solo en LRU

    def set_policy(self, policy):
        if policy not in ["LRU", "FIFO"]:
            raise ValueError("Política no soportada")
        self.policy = policy

    def add(self, item):
        if item in self.cache:
            if self.policy == 'LRU':
                self.order.remove(item)
                self.order.append(item)
            return

        if len(self.cache) == self.capacity:
            if self.policy == 'FIFO':
                self.cache.pop(0)
            elif self.policy == 'LRU':
                lru_item = self.order.popleft()
                self.cache.remove(lru_item)

        self.cache.append(item)
        if self.policy == 'LRU':
            self.order.append(item)

    def get(self, item):
        if item in self.cache:
            if self.policy == 'LRU':
                self.order.remove(item)
                self.order.append(item)
            return item
        return None

    def items(self):
        return self.cache

