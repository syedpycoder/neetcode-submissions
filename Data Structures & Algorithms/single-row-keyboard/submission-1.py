class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:

        charDict = {}
        currentPos = 0
        total = 0
        
        for pos, ch in enumerate(keyboard):
            charDict[ch] = pos
        
        for ch in word:
            newPos = charDict[ch]
            total += abs(newPos - currentPos)
            currentPos = newPos

        return total    
