class Solution:

    def stringComputeLeft(self, subs):
        total_zero = 0
        for ch in subs:
            if ch == '0':
                total_zero += 1   
        return total_zero

    def stringComputeRight(self, subs):
        total_ones = 0
        for ch in subs:
            if ch == '1':
                total_ones += 1   
        return total_ones    

    def maxScore(self, s: str) -> int:
        maxScore = 0
        n = len(s)
        for i in range(n):
            left = s[:i+1]
            right = s[i+1:]
            if left and right:
               total = self.stringComputeLeft(left) + self.stringComputeRight(right)
               maxScore = max(maxScore, total)
        
        return maxScore    

        