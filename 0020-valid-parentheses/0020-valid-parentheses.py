class Solution:
    def isValid(self, s: str) -> bool:
        stack = []                              # Keeps track of open brackets

        mapping = {                             # Maps closing → opening bracket
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in mapping:                 # It's a CLOSING bracket
                top = stack.pop() if stack else '#'   # Get last open bracket
                if mapping[char] != top:        # Does it match?
                    return False                # Mismatch → invalid
            else:
                stack.append(char)             # It's an OPENING bracket → push

        return len(stack) == 0                 # Valid only if nothing left