class Solution:
    def subarraysWithMoreOnesThanZeroes(self, nums: List[int]) -> int:     


        n = len(nums)
        result = 0
        for right in range(n):
            greater = 0
            for left in range(right, n):

                if nums[left] == 1:
                    greater += 1
                else:
                    greater -= 1

                if greater > 0:
                    result += 1
        return result % 1000000007                   






