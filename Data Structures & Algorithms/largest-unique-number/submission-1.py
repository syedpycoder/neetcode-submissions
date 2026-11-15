class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:

        numDict = collections.Counter(nums)

        sortedNum = sorted(numDict.keys(), reverse = True)

        for num in sortedNum:
            if numDict[num] == 1:
                return num
        return -1        

        