class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stack = []

        for digit in num:

            # Remove larger previous digits
            while k > 0 and stack and stack[-1] > digit:

                stack.pop()
                k -= 1

            stack.append(digit)

        # If removals still left
        while k > 0:

            stack.pop()
            k -= 1

        # Convert to string
        result = "".join(stack)

        # Remove leading zeros
        result = result.lstrip('0')

        # Empty string means 0
        return result if result else "0"