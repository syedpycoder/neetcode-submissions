class MinStack:

    def __init__(self):
        self.stack = []
       
       
  
    def push(self, val: int) -> None:
        if self.stack:
            min_val = self.stack[-1][0]
            min_val = min(min_val, val)
            self.stack.append((min_val, val))
        else:
            self.stack.append((val,val))    
      
               
    
    def pop(self) -> None:
        self.stack.pop()
      
       
       
       
    def top(self) -> int:
        return self.stack[-1][1]
    
       
       
        
    def getMin(self) -> int:
        return self.stack[-1][0]
       
       
        
        
