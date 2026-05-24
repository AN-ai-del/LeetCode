class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []                      # Acts as our "processed" string

        for char in s:
            if stack and stack[-1] == char:   # Top of stack matches current
                stack.pop()                   # They cancel each other out
            else:
                stack.append(char)            # No match → push it

        return ''.join(stack)           # Rebuild string from stack