class Solution:
    def findLucky(self, arr: List[int]) -> int:
        maxNum = -1
        numDict = collections.Counter(arr)
        for num in numDict:
            if numDict[num] == num:
                maxNum = max(maxNum, num)
        return maxNum        
        