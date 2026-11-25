class Solution:
    def maxScore(self, s: str) -> int:

        ones = s.count('1')
        zeros = 0
        maxScore = 0
        n = len(s)

        for i in range(n-1):

            if s[i] == '0':
                zeros += 1
            else:
                ones -= 1

            maxScore = max(maxScore, ones+zeros)

        return maxScore            
        