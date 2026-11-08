class Solution:
    def subarraysWithMoreOnesThanZeroes(self, nums: List[int]) -> int:

        prefix = {0:1}
        result = 0
        balance = 0
        resultSubArr = 0


        for num in nums:

            if num == 1:
                resultSubArr += prefix.get(balance, 0)
                balance += 1
            else:
                balance -= 1
                resultSubArr -= prefix.get(balance, 0)

            result += resultSubArr
            
            result %= 1000000007

            if balance not in prefix:
                prefix[balance] = 1
            else:
                prefix[balance] += 1
        
        return result                 





