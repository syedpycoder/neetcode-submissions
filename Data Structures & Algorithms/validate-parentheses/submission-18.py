class Solution:
    def isValid(self, s: str) -> bool:

        char_dict = {'}':'{', ')':'(', ']':'['}
        stack = []

        for ch in s:
            if ch not in char_dict.keys():
                stack.append(ch)
            else:
                if stack and stack[-1] == char_dict[ch]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0                     

       
