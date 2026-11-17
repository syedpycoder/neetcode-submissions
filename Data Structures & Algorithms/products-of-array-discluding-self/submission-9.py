class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        prod = [1] * n

        left = 1
        right = 1

        for i in range(n):
            nums[i] = left
            prod[i] *= left

        for j in range(n-1,-1,-1):
            prod[j] *= right
            right *= nums[j]

        return prod        

       