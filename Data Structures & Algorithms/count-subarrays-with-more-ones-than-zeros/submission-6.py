class Solution:
    def subarraysWithMoreOnesThanZeroes(self, nums: List[int]) -> int:

        prefixSum = {0:1}
        current = 0
        total_valid_sub = 0
        result = 0

        for num in nums:

            if num == 1:
                total_valid_sub += prefixSum.get(current, 0)
                current += 1
            else:
                current -= 1
                total_valid_sub -= prefixSum.get(current, 0)
                

            result += total_valid_sub
            result %= 1000000007

            if current not in prefixSum:
                prefixSum[current] = 1
            else:
                prefixSum[current] += 1

        return result                     

