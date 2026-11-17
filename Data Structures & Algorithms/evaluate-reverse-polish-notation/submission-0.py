class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [0]
        for ch in tokens:
            if ch.isdigit():
                stack.append(int(ch))
            else:
                if ch == '+':
                    val = stack[-1] + stack[-2]
                    stack.append(val)
                elif ch == '-':
                    val = stack[-1] - stack[-2]
                    stack.append(val)
                elif ch == '*':
                    val = stack[-1] * stack[-2]
                    stack.append(val)
                elif ch == '/':
                    val = stack[-1] // stack[-2]
                    stack.append(val)
        return stack[-1]                

        