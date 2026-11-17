class MyHashMap:

    def __init__(self):
        self.keys = []
        self.values = []
        

    def put(self, key: int, value: int) -> None:
        if key not in self.keys:
            self.keys.append(key)
            self.values.append(value)
        else:
            for k, v in enumerate(self.keys):
                if v == key:
                    break
                else:
                    continue
            self.values[k] = value                
        

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1

        for k, v in enumerate(self.keys):
            if v == key:
                break
            else:
                continue
        return self.values[k]             
        

    def remove(self, key: int) -> None:
        for k, v in enumerate(self.keys):
            if v == key:
                break
            else:
                continue
        self.keys.pop(k)
        self.values.pop(k)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)