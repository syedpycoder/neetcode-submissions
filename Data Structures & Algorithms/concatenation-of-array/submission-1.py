class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        j = 0
        m = 2 * n
        ans = [0] * m
        for i in range(m):
            if j < n:
                ans[i] = nums[j]
                j += 1
            else:
                j = 0
                ans[i] = nums[j]
                j += 1
        return ans        



        