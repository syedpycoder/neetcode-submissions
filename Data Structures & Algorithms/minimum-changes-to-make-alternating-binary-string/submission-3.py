class Solution:
    def minOperations(self, s: str) -> int:

        current = 0
        cnt0 = 0

        for ch in s:
            if int(ch) != current:
                cnt0 += 1
            current ^= 1

        current = 1
        cnt1 = 0

        for ch in s:
            if int(ch) != current:
                cnt1 += 1
            current ^= 1

        return min(cnt0, cnt1)                
        