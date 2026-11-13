class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:

        minNum = min(nums)
        maxNum = max(nums)
        rangeNum = list(range(minNum, maxNum+1))
        return rangeNum == sorted(nums)

        