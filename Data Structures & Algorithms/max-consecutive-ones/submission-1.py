class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        

        n = len(nums)
        maxCount = 0
        count = 0

        for i in range(n):
            if nums[i] == 1:
                count += 1
            else:
                count = 0
            maxCount = max(count, maxCount)
        maxCount = max(count, maxCount)
        return maxCount    