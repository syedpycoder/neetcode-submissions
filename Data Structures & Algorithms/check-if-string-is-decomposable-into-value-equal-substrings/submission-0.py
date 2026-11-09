class Solution:
    def isDecomposable(self, s: str) -> bool:

        n = len(s)
        left = right = 0
        count_two = 0
        count_three = 0
        while right < n:
            count = 0
            while left < n and s[left] == s[right]:
                count += 1
                left += 1
            
            if count % 3 == 1:
                return False

            if count % 3 == 2:
                count_two += 1

            if count_two > 1:
                return False        

            right = left 

        return count_two == 1        

       