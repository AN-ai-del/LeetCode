class Solution:
    def longestPalindrome(self, s: str) -> int:

        freq = {}

        # Count frequency of each character
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        length = 0
        odd_found = False

        # Process frequencies
        for count in freq.values():

            # Add even part
            length += (count // 2) * 2

            # Check if odd exists
            if count % 2 == 1:
                odd_found = True

        # One odd character can sit in center
        if odd_found:
            length += 1

        return length