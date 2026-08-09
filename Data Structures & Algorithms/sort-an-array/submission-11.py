class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        maxNum = max(nums)
        minNum = min(nums)

        numDict = collections.Counter(nums)

        index = 0

        for num in range(minNum, maxNum+1):
            while numDict[num] > 0:
                nums[index] = num
                numDict[num] -= 1
                index += 1

        return nums        

       