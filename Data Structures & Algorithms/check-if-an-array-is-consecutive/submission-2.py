class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:

        maxNum = max(nums)
        minNum = min(nums)
        consecutiveNums = list(range(minNum, maxNum+1))
        return consecutiveNums == sorted(nums)

       