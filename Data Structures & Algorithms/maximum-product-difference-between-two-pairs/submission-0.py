class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        sortedNums = sorted(nums, reverse=True)
        result = (sortedNums[0]*sortedNums[1]) - (sortedNums[-1]*sortedNums[-2])
        return result
        