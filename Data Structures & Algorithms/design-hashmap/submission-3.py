class MyHashMap:

    def __init__(self):
        self.arr = []
        self.bucket = set()
        

    def put(self, key: int, value: int) -> None:
        if key not in self.bucket:
            self.arr.append((key, value))
            self.bucket.add(key)
        else:
            for i in range(len(self.arr)):
                x, y = self.arr[i]
                if x == key:
                    self.arr[i] = (key, value)
                    break
                else:
                    continue    

        

    def get(self, key: int) -> int:
        if key not in self.bucket:
            return -1
        else:
            for i in range(len(self.arr)):
                x, y = self.arr[i]
                if x == key:
                    return y
                else:
                    continue        
        

    def remove(self, key: int) -> None:
        if key in self.bucket:
            self.bucket.remove(key)
            for i in range(len(self.arr)):
                x, y = self.arr[i]
                if x == key:
                    pos = i
                    break
                else:
                    continue
            self.arr.pop(pos)        

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)