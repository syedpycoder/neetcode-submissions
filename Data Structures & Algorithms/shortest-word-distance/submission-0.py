class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:

        charDict = {}
        shortDistance = float('inf')
        for pos, value in enumerate(wordsDict):
            if value not in charDict:
                charDict[value] = [pos]
            else:
                charDict[value].append(pos)

        for num1 in charDict[word1]:
            for num2 in charDict[word2]: 
                shortDistance = min(abs(num2-num1),shortDistance)

        return shortDistance                   
        