class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.my_dict = dict()
        self.order = list()

    def get(self, key: int) -> int:
        if key in self.my_dict:
            self.order.remove(key)       # move to most recently used
            self.order.append(key)
            return self.my_dict[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.my_dict:
            self.order.remove(key)       # remove old position
        elif len(self.my_dict) == self.capacity:
            lru = self.order.pop(0)      # evict least recently used
            self.my_dict.pop(lru)
        self.my_dict[key] = value
        self.order.append(key)           # mark as most recently used