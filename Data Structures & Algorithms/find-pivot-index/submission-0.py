class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        totalSum = sum(nums)
        total = 0

        for pos, val in enumerate(nums):
            
            if total == (totalSum - total - val):
                return pos

            total += val 

        return -1      
                  