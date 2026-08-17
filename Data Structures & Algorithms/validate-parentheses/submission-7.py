class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        char_dict = {'}':'{',']':'[',')':'('}

        for ch in s:
            if ch in char_dict.values():
                stack.append(ch)
            else:
                if stack and stack[-1] == char_dict[ch]:
                    stack.pop()
                else:
                    return False

        if not stack:
            return True
        return False                

