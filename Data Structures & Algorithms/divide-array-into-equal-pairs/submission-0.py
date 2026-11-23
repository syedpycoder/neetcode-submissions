class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        numDict = collections.Counter(nums)
        for num in numDict:
            if numDict[num] % 2 == 1:
                return False
        return True        