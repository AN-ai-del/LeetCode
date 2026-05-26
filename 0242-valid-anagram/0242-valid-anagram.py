class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):                # Quick length check
            return False

        count = [0] * 26                    # One slot per letter a-z

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1  # Increment for s
            count[ord(t[i]) - ord('a')] -= 1  # Decrement for t

        return all(c == 0 for c in count)   # All zeros = perfect match