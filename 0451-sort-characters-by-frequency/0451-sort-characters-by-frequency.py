from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)

        # Sort characters by frequency in descending order
        sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        # Build the result string
        result = ''.join(char * count for char, count in sorted_chars)

        return result