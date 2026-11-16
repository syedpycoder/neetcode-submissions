class StringIterator:

    def __init__(self, compressedString: str):
        self.uncompressed = ''
        currentString = ''
        currentCount = '0'
        for i in range(len(compressedString)):
            if compressedString[i].isalpha():
                #print(compressedString[i])
                self.uncompressed += currentString * int(currentCount)
                #print(self.uncompressed)
                currentString = compressedString[i]
                currentCount = '0'
            elif compressedString[i].isdigit():
                #print(compressedString[i])
                #print(currentCount)
                currentCount += compressedString[i]
        self.uncompressed += currentString * int(currentCount)                        

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
