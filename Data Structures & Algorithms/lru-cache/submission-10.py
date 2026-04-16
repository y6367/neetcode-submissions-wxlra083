class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.my_dict = dict()
        self.order = list()
        

    def get(self, key: int) -> int:
        if key in self.my_dict:
            self.order.pop(self.order.index(key))
            self.order.append(key)
            return self.my_dict.get(key)
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.my_dict:
            self.my_dict.update({key: value})
            self.order.pop(self.order.index(key))
            self.order.append(key)
        elif len(self.my_dict) == self.capacity:
            popped = self.order.pop(0)
            self.my_dict.pop(popped)
            self.my_dict[key] = value
            self.order.append(key)
        else:
            self.my_dict[key] = value
            self.order.append(key)

