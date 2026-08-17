class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token.lstrip('-').isdigit():
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()
                if token == '+':
                    val = b + a
                    stack.append(val)
                elif token == '-':
                    val = b-a
                    stack.append(val)
                elif token == '*':
                    val = b * a
                    stack.append(val)
                elif token == '/':
                    val = int(b/a)
                    stack.append(val)
        return stack[0]                        

       