class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        count = 0
        n = len(s)

        for right in range(n):
            subs = ''
            for left in range(right, n):
                subs += s[left]
                if subs[0] == subs[-1]:
                    count += 1
        return count            
                  



