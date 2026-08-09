class StringIterator:

    def __init__(self, compressedString: str):
        self.ptr = 0
        self.uncompressed = ''
        i = 0
        while i < len(compressedString):
            ch = compressedString[i]
            current_number = 0
            if ch.isdigit():
                while i < len(compressedString) and compressedString[i].isdigit():
                    current_number = current_number * 10 + int(compressedString[i])
                    i += 1
                self.uncompressed += self.uncompressed[-1] * (current_number - 1)   
            else:
                self.uncompressed += ch
                i += 1            
     
    
    def next(self) -> str:

        if not self.hasNext():
            return ''
        ch = self.uncompressed[self.ptr] 
        self.ptr += 1
        return ch   
          

            
    def hasNext(self) -> bool:
        return self.ptr != len(self.uncompressed)
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
