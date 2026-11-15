class Solution:
    def scoreOfString(self, s: str) -> int:

        total = 0
        n = len(s)

        for i in range(1, n):
            total += abs(ord(s[i]) - ord(s[i-1]))

        return total    
        