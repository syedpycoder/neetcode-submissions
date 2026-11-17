class StringIterator:

    def __init__(self, compressedString: str):
        self.uncompressed = ''
        for i in range(0, len(compressedString), 2):
            self.uncompressed += compressedString[i] * int(compressedString[i+1])
        self.n = len(self.uncompressed)
        self.current = 0    
        

    def next(self) -> str:
        if self.hasNext():
            currentChar = self.uncompressed[self.current]
            self.current += 1
            return currentChar
        else:
            return ' '    
        

    def hasNext(self) -> bool:
        return self.current < self.n


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
