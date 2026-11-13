class Solution:
    def isDecomposable(self, s: str) -> bool:

        n = len(s)
        count_two = 0
        left = right = 0

        while left < n:
            count = 0
            while right < n and s[left] == s[right]:
                count += 1
                right += 1

            if count % 3 == 1:
                return False    

            if count % 3 == 2:
                count_two += 1

            if count_two > 1:
                return False

            left = right
        
        return count_two == 1                 
