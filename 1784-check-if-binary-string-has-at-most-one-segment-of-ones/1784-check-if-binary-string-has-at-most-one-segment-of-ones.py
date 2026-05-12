class Solution:
    def checkOnesSegment(self, s: str) -> bool:

        found_zero = False

        for ch in s:

            # Once zero appears
            if ch == '0':
                found_zero = True

            # If 1 appears again after zero
            elif found_zero:
                return False

        return True