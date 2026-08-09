class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        prod = [1] * n
        pref = [1] * n
        pos = [1] * n
        
        prefix = 1
        for i in range(n):
            prefix *= nums[i]
            pref[i] *= prefix

        post = 1
        for j in range(n-1,-1,-1):
            post *= nums[j]
            pos[j] *= post    

        for i in range(n):
            if i-1 < 0: 
                prefixProd = 1
            else:
                prefixProd = pref[i-1]

            if i+1 >= n:
                postProd = 1
            else:
                postProd = pos[i+1]

            prod[i] = prefixProd * postProd 

        return prod                     