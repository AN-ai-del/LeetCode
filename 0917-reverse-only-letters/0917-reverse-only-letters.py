class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

        # Convert string to list because strings are immutable
        arr = list(s)

        left = 0
        right = len(arr) - 1

        while left < right:

            # Skip non-letters from left
            while left < right and not arr[left].isalpha():
                left += 1

            # Skip non-letters from right
            while left < right and not arr[right].isalpha():
                right -= 1

            # Swap letters
            arr[left], arr[right] = arr[right], arr[left]

            left += 1
            right -= 1

        return "".join(arr)