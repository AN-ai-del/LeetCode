class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        # Dictionary to store frequency of each string
        freq = {}

        # Count frequency
        for s in arr:
            if s in freq:
                freq[s] += 1
            else:
                freq[s] = 1

        # Find kth distinct string
        count = 0

        for s in arr:

            # Distinct means appears only once
            if freq[s] == 1:

                count += 1

                # If kth distinct found
                if count == k:
                    return s

        # If less than k distinct strings
        return ""