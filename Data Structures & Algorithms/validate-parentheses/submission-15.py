class Solution:
    def isValid(self, s: str) -> bool:

        char_dict = {'}':'{', ')':'(', ']':'['}
        stack = []

        for ch in s:
            if ch not in char_dict.keys():
                stack.append(ch)
            else:
                if char_dict[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        return False                        

       
