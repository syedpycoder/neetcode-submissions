class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        splitS1 = s1.split(" ")
        splitS2 = s2.split(" ")
        combined = splitS1 + splitS2
        result = []
        freqDict = collections.Counter(combined)
        for word in freqDict:
            if freqDict[word] == 1:
                result.append(word)
        return result        

