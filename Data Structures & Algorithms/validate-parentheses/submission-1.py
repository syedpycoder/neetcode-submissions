class Solution:
    def isValid(self, s: str) -> bool:
        

        stack = [] 
        stack_dict = {'}':'{',']':'[',')':'('}

        for ch in s:
            if ch == '{' or ch == '[' or ch == '(':
                stack.append(ch)
            else:
                if stack and stack[-1] == stack_dict[ch]:
                    stack.pop()
                else:
                    return False    

        if not stack:
            return True
        return False                     
      