class Solution:
    def subarraysWithMoreOnesThanZeroes(self, nums: List[int]) -> int:

        prefix_balance = {0:1}
        balance = 0
        total_valid_sub = 0
        result = 0


        for num in nums:

            if num == 1:
                total_valid_sub += prefix_balance.get(balance, 0)
                balance += 1
            else:
                balance -= 1
                total_valid_sub -= prefix_balance.get(balance, 0)

            result += total_valid_sub
            result %= 1000000007

            prefix_balance[balance] = prefix_balance.get(balance, 0) + 1

        return result            
