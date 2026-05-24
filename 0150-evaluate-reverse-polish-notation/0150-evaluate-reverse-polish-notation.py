class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []                                  # Stores numbers/results

        for token in tokens:
            if token == '+':
                b, a = stack.pop(), stack.pop()     # Pop last two numbers
                stack.append(a + b)                 # Push result

            elif token == '-':
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)

            elif token == '*':
                b, a = stack.pop(), stack.pop()
                stack.append(a * b)

            elif token == '/':
                b, a = stack.pop(), stack.pop()
                stack.append(int(a / b))            # Truncate toward zero

            else:
                stack.append(int(token))            # It's a number → push

        return stack[0]                             # Final answer