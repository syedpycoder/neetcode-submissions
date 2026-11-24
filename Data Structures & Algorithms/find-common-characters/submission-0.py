class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        minStrs = set(min(words, key = len))
        result = []
        for ch in minStrs:
            countArr = []
            for word in words:
                countCh = word.count(ch)
                countArr.append(countCh)
            minVal = min(countArr)
            result += [ch] * minVal
        return result        
        