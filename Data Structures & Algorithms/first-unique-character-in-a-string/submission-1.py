class Solution:
    def firstUniqChar(self, s: str) -> int:

        charDict = {}
        for pos, ch in enumerate(s):
            if ch not in charDict:
                charDict[ch] = [pos]
            else:
                charDict[ch].append(pos)

        for ch in charDict:
            if len(charDict[ch]) == 1:
                return charDict[ch][0]
        return -1                    
        