class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        maxSum = nums[0]
        currentSum = nums[0]
        n = len(nums)

        for i in range(1, n):
            if nums[i] > nums[i-1]:
                currentSum += nums[i]
            else:
                currentSum = nums[i]
            maxSum = max(currentSum, maxSum)
        return maxSum            