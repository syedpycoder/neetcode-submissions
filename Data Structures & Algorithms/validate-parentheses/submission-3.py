class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        char_set = {'{':'}', '[':']','(':')'}
        for ch in s:
            if ch in char_set.keys():
                stack.append(ch)
            else:
                char = stack.pop()
                if ch == char_set[char]:
                    continue
                else:
                    return False
        return True                    
        

        