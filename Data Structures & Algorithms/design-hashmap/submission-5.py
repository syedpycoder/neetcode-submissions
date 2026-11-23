class MyHashMap:

    def __init__(self):
        self.keys = []
        self.values = []
        
    def put(self, key: int, value: int) -> None:
        if key not in self.keys:
            self.keys.append(key)
            self.values.append(value)
        else:
            pos = self.keys.index(key)
            self.values[pos] = value

    def get(self, key: int) -> int:
        if key in self.keys:
            pos = self.keys.index(key)
            return self.values[pos]
        else:
            return -1    

    def remove(self, key: int) -> None:
        if key in self.keys:
            pos = self.keys.index(key)
            self.keys.pop(pos)
            self.values.pop(pos)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)