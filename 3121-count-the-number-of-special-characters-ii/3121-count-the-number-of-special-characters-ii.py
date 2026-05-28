class Solution:
    def numberOfSpecialChars(self, word: str) -> int:

        last_lower = {}
        first_upper = {}

        # Store positions
        for i, ch in enumerate(word):

            if ch.islower():
                last_lower[ch] = i

            else:
                lower = ch.lower()

                if lower not in first_upper:
                    first_upper[lower] = i

        ans = 0

        # Check all letters
        for ch in last_lower:

            if ch in first_upper:

                if last_lower[ch] < first_upper[ch]:
                    ans += 1

        return ans