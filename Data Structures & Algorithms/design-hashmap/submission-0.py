class MyHashMap:

    def __init__(self):
        self.bucket = []
        

    def put(self, key: int, value: int) -> None:
        flag = False
        pos_idx = -1
        for pos, element in enumerate(self.bucket):
            key_element = element[0]
            if key == key_element:
                flag = True
                pos_idx = pos
                break
            else:
                continue
        if flag:
            self.bucket[pos_idx] = [key, value]
        else:
            self.bucket.append([key, value])                
        

    def get(self, key: int) -> int:
        for element in self.bucket:
            key_element = element[0]
            if key_element == key:
                return element[1]
            else:
                continue
        return -1            
        

    def remove(self, key: int) -> None:
        for pos, element in enumerate(self.bucket):
            key_element = element[0]
            if key_element == key:
                self.bucket.pop(pos)
            else:
                continue    
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)