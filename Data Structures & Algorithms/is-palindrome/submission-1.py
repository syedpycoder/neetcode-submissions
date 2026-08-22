class Solution:
    def isPalindrome(self, s: str) -> bool:

       

        char_string = ''

        for ch in s:
            if ch.isalpha() or ch.isdigit():
                char_string += ch.lower()
            else:
                continue 

        L = 0
        R = len(char_string) - 1           

        while L < R:
            if char_string[L] != char_string[R]:
                return False
            L += 1
            R -= 1
        return True        
        