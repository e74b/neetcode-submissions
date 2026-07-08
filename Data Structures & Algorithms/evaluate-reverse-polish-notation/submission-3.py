
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        for token in tokens:
            try:
                number = int(token)
                stack.append(number)
            except ValueError:
                b = stack.pop(-1)
                a = stack.pop(-1)
                
                if token == "+": stack.append(a + b)
                elif token == "-": stack.append(a - b)
                elif token == "*": stack.append(a * b)
                elif token == "/": stack.append(int(a / b))
        
        return stack[0]