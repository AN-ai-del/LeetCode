class Solution:
    def numberOfSpecialChars(self, word: str) -> int:

        letters = set(word)

        count = 0

        for ch in letters:

            # Check lowercase letters only
            if ch.islower() and ch.upper() in letters:
                count += 1

        return count