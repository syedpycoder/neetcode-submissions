class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        char_dict = {}

        for ch in s:
            if ch not in char_dict:
                char_dict[ch] = 1
            else:
                char_dict[ch] += 1

        odd_count = 1

        for ch in char_dict:
            if char_dict[ch] % 2 == 1:
                odd_count -= 1
                if odd_count < 0:
                    return False
            elif char_dict[ch] % 2 == 0:
                continue        
        return True                        
        