class HashTable:
    
    def __init__(self, capacity: int):
        self.my_dict = dict()
        self.capacity = capacity


    def insert(self, key: int, value: int) -> None:
        if key in self.my_dict:
            self.my_dict.update({key: value})
        else:
            self.my_dict[key] = value
            if (len(self.my_dict) / self.capacity) >= 0.5:
                self.capacity *= 2


    def get(self, key: int) -> int:
        if key in self.my_dict:
            return self.my_dict[key]
        else:
            return -1


    def remove(self, key: int) -> bool:
        if key in self.my_dict:
            self.my_dict.pop(key)
            return True
        else:
            return False


    def getSize(self) -> int:
        return len(self.my_dict)


    def getCapacity(self) -> int:
        return self.capacity


    def resize(self) -> None:
        self.capacity *= 2

