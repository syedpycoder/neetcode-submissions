class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        
        pos_s = 0

        for pos, ch in enumerate(t):

            if ch == s[pos_s]:
                pos_s += 1
        print(pos_s)
        return pos_s == len(s)        

        



        