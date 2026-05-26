class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = [0] * 26                        # One slot per letter a-z

        for char in magazine:
            count[ord(char) - ord('a')] += 1    # Add available letters

        for char in ransomNote:
            count[ord(char) - ord('a')] -= 1    # Use up letters
            if count[ord(char) - ord('a')] < 0: # Ran out of this letter
                return False

        return True