class StringIterator:

    def __init__(self, compressedString: str):
        self.ptr = 0
        self.nums = []
        self.char = []

        for i in range(len(compressedString)):
            if not compressedString[i].isdigit():
                self.char.append(compressedString[i])

        digit = ''
        for j in range((len(compressedString))):
            if compressedString[j].isdigit():
                digit += compressedString[j]
            else:
                if digit:
                   self.nums.append(int(digit))
                digit = ''
        self.nums.append(digit)        

        
     
    
    def next(self) -> str:

        if not self.hasNext():
            return ''

        self.nums[self.ptr] -= 1
        ch = self.char[self.ptr]
        if self.nums[self.ptr] == 0:
            self.ptr += 1
        return ch    


      

            
    def hasNext(self) -> bool:
        return self.ptr != len(self.char)
        
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
