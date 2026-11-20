class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:

        maxIncreasing = 1
        maxDecreasing = 1
        increasing = 1
        decreasing = 1
        n = len(nums)

        for i in range(1, n):

            if nums[i] > nums[i-1]:
                increasing += 1
                decreasing = 1
            elif nums[i] < nums[i-1]:
                decreasing += 1
                increasing = 1  
            elif nums[i] == nums[i-1]:
                decreasing = 1
                increasing = 1
            maxIncreasing = max(maxIncreasing, increasing)
            maxDecreasing = max(maxDecreasing, decreasing)
        
            



        return max(maxDecreasing,maxIncreasing)        


        