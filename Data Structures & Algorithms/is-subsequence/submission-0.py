class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        n = len(t)
        pos_sub = 0
        for i in range(n):
            if pos_sub < len(s) and s[pos_sub] == t[i]:
                pos_sub += 1

        if pos_sub == len(s):
            return True
        return False            
       