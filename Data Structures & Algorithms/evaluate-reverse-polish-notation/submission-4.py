class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch.isdigit():
                stack.append(int(ch))
            else:
                a = stack.pop()
                b = stack.pop()
                if ch == '+':
                    stack.append((a+b))
                elif ch == '-':
                    stack.append((b-a))
                elif ch == '*':
                    stack.append((b*a))
                elif ch == '/':
                    stack.append(int(float(b)/a))
        return stack[-1]                

        