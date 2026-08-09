class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.i1 = 0
        self.i2 = 0
        self.count = 0
        

    def next(self) -> int:
        if self.count % 2 == 0:
            if self.i1 < len(self.v1):
                val = self.v1[self.i1]
                self.i1 += 1
            else:
                if self.hasNext():
                    val = self.v2[self.i2]
                    self.i2 += 1    
        else:
            if self.i2 < len(self.v2):
                val = self.v2[self.i2]
                self.i2 += 1
            else:
                if self.hasNext():
                    val = self.v1[self.i1]
                    self.i1 += 1    
        self.count += 1
        return val            
         

    def hasNext(self) -> bool:
        if self.i1 < len(self.v1) or self.i2 < len(self.v2):
            return True
        return False   
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
