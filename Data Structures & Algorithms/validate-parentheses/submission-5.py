class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        char_set = {'}':'{', ']':'[',')':'('}
        for ch in s:
            if ch in char_set.values():
                stack.append(ch)
            else:
                if stack and stack[-1] == char_set[ch]:
                   stack.pop()
                else:
                    return False
        if not stack:
            return True
        return False                   

                

        