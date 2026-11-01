class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        pass
        #[5,-9,6]
        #prefix = [5, -4, 2]
        #postfix =[2,-3,6]

        #[-8, -2, -7]
        #prefix = [-8, -10, -17]
        #postfix =[-17,-9,-7]
        #result = max(-7, -17) => -7

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

            


