class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        

        n = len(s)
        result = set()

        for start in range(n):
            subDict = {}
            sub = ''
            for end in range(start, n):
                
                sub += s[end]

                if s[end] not in subDict:
                    subDict[s[end]] = 1
                else:
                    subDict[s[end]] += 1

                freqVal = list(subDict.values())

                if len(set(freqVal)) == 1:
                    result.add(sub)

        return len(result)            


