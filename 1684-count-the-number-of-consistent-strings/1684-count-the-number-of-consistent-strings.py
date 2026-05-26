class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        allowed_set = set(allowed)          # O(1) lookup
        count = 0

        for word in words:
            is_consistent = True

            for char in word:
                if char not in allowed_set: # Found disallowed char
                    is_consistent = False
                    break                   # Early exit

            if is_consistent:
                count += 1

        return count