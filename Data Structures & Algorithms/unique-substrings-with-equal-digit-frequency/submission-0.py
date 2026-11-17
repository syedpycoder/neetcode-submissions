class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        

        n = len(s)
        result = set()

        for start in range(n):
            for end in range(start+1, n+1):
                sub = s[start:end]
                subDict = collections.Counter(sub)
                freqVal = list(subDict.values())
                if len(set(freqVal)) == 1:
                    result.add(sub)
                else:
                    continue    
        return len(result)            


