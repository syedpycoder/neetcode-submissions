class Solution:
    def subarraysWithMoreOnesThanZeroes(self, nums: List[int]) -> int:

        result = 0
        n = len(nums)

        for right in range(n):
            StrictlyGreater = 0
            for left in range(right, n):

                if nums[left] == 1:
                    StrictlyGreater += 1
                else:
                    StrictlyGreater -= 1

                if StrictlyGreater > 0:
                    result += 1
        
        return result                    


        
        

        