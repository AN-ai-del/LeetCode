class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []                          # Stores valid directory names

        parts = path.split('/')            # Split by '/' into tokens

        for part in parts:
            if part == '' or part == '.':  # Empty or current dir → skip
                continue
            elif part == '..':             # Parent dir → go back
                if stack:                  # Only pop if not already at root
                    stack.pop()
            else:
                stack.append(part)         # Valid name → push to stack

        return '/' + '/'.join(stack)       # Rebuild the clean path