class TwoSum:
    def __init__(self):
        self.nums = []
        self.numDict = {}
        self.pos = 0
    
    def add(self, number: int) -> None:
        self.nums.append(number)
        self.numDict[number] = self.pos
        self.pos += 1

    def find(self, value: int) -> bool:
        
        for p, v in enumerate(self.nums):
            complement = value - v
            if complement in self.numDict and self.numDict[complement] != p:
                return True
        return False        

