class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        charDict = {}
        count = 0

        for ch in s:
            if ch not in charDict:
                charDict[ch] = 1
            else:
                charDict[ch] += 1

            count += charDict[ch]    

        return count    


        


