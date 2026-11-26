class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        longestString = -1
        charDict = {}
        for pos, ch in enumerate(s):
            if ch not in charDict:
                charDict[ch] = [pos]
            else:
                charDict[ch].append(pos)

        for ch in charDict:
            if len(charDict[ch]) > 1:
                currentLength = (charDict[ch][-1] - charDict[ch][0]) - 1
                longestString = max(currentLength, longestString)

        return longestString        
                            
        