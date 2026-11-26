class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        
        n = len(words)
        stringJoin = ''.join(words)
        charDict = collections.Counter(stringJoin)

        for ch in charDict:
            if charDict[ch] % n != 0:
                return False
        return True                        