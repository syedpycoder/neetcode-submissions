class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        prod = [1] * n

        left = 1
        right = 1

        for i in range(n):
            prod[i] = left
            left *= nums[i]
            
        for j in range(n-1,-1,-1):
            prod[j] *= right
            right *= nums[j]

        return prod        

       