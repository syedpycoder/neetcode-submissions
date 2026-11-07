class Solution:
    def subarraysWithMoreOnesThanZeroes(self, nums: List[int]) -> int:

        result = 0
        prefixSum = {0:1}
        current_subArr = 0
        balance = 0

        for num in nums:

            if num == 1:
                current_subArr += prefixSum.get(balance, 0)
                balance += 1
            else:
                balance -= 1
                current_subArr -= prefixSum.get(balance, 0)

            result += current_subArr 
            result %= 1000000007
            if balance not in prefixSum:
                prefixSum[balance] = 1
            else:
                prefixSum[balance] += 1

        return result                   
