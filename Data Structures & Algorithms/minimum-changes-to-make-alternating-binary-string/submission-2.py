class Solution:
    def minOperations(self, s: str) -> int:

        cnt0 = 0
        cur = 0
        for ch in s:
            if int(ch) != cur:
                cnt0 += 1
            cur = cur^1

        cnt1 = 0
        cur = 1

        for ch in s:
            if int(ch) != cur:
                cnt1 += 1
            cur = cur^1

        return min(cnt1, cnt0)                
        