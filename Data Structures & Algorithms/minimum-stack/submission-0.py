class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = float('inf')
        

    def push(self, val: int) -> None:
        if val < self.minVal:
            self.minVal = val    
        self.stack.append((self.minVal, val))
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][1]

    def getMin(self) -> int:
        return self.stack[-1][0]
        
