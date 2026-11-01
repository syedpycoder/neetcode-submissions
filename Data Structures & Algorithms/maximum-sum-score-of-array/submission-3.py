class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
    
        n = len(nums)
        prefix = [0] * n
        postfix = [0] * n
        
        pre_fix = 0
        post_fix = 0
        max_val = float('-inf')
        
        for i in range(n):
            pre_fix += nums[i]
            prefix[i] = pre_fix

        for j in range(n-1, -1, -1):
            post_fix += nums[j]
            postfix[j] = post_fix

        for i in range(n):
            max_post_pre = max(prefix[i], postfix[i])
            max_val = max(max_post_pre, max_val)

        return max_val    

            


