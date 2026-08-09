class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        prefix = 1
        postfix = 1
        prod = [1] * n

        for i in range(n):
            prod[i] = prefix
            prefix *= nums[i]

        for j in range(n-1,-1,-1):
            prod[j] *= postfix
            postfix *= nums[j] 

        return prod       