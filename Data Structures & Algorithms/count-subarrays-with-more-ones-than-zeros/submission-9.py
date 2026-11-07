class Solution:
    def subarraysWithMoreOnesThanZeroes(self, nums: List[int]) -> int:

        prefix = {0:1}
        result = 0
        currentSubArr = 0
        balance = 0

        for num in nums:

            if num == 1:
                currentSubArr += prefix.get(balance, 0)
                balance += 1
            else:
                balance -= 1
                currentSubArr -= prefix.get(balance, 0) 
                

            result += currentSubArr
            result %= 1000000007

            if balance not in prefix:
                prefix[balance] = 1
            else:
                prefix[balance] += 1
        
        return result                  
