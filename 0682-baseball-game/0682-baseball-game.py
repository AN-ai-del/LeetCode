class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []                                      # Our scoreboard

        for op in operations:
            if op == 'C':
                stack.pop()                             # Remove last score
            elif op == 'D':
                stack.append(stack[-1] * 2)             # Double last score
            elif op == '+':
                stack.append(stack[-1] + stack[-2])     # Sum of last two
            else:
                stack.append(int(op))                   # It's a number

        return sum(stack)                               # Final answer