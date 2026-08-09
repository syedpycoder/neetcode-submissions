class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        numDict = collections.Counter(nums)
        minNum = min(nums)
        maxNum = max(nums)
        index = 0

        for num in range(minNum, maxNum+1):
            if num in numDict.keys():
                while numDict[num] > 0:
                    nums[index] = num
                    index += 1
                    numDict[num] -= 1

        return nums