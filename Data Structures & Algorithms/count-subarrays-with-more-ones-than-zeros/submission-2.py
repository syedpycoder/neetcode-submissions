class Solution:
    def subarraysWithMoreOnesThanZeroes(self, nums: List[int]) -> int:

        
        result = 0

        n = len(nums)

        for right in range(n):
            for left in range(right, n):
                arr = nums[right:left+1]

                if arr.count(1) > arr.count(0):
                    result += 1
        return result             


        