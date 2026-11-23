class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        increasing = 0
        decreasing = 0
        n = len(nums)

        for i in range(1, n):
            if nums[i] >= nums[i-1]:
                increasing += 1
            if nums[i] <= nums[i-1]:
                decreasing += 1

        if increasing == n-1 or decreasing == n-1:
            return True
        return False                
        