class Solution:
    def subarraysWithMoreOnesThanZeroes(self, nums: List[int]) -> int:

        prefixSum = {0:1}
        result = 0
        balance = 0
        currentSubArr = 0

        for num in nums:

            if num == 1:
                currentSubArr += prefixSum.get(balance, 0)
                balance += 1
            else:
                balance -= 1
                currentSubArr -= prefixSum.get(balance, 0)

            result += currentSubArr
            result %= 1000000007

            if balance not in prefixSum:
                prefixSum[balance] = 1
            else:
                prefixSum[balance] += 1

        return result                    
