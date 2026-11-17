class StringIterator:

    def __init__(self, compressedString: str):
        self.point = 0
        self.string = ''
        for i in range(0,len(compressedString),2):
            self.string += compressedString[i] * int(compressedString[i+1]) 
    
    def next(self) -> str:
        next_str = self.string[self.point:]
        if next_str:
            self.point += 1
            return next_str[0]
        return ' '    

            
    def hasNext(self) -> bool:
        return self.point < len(self.string)


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
