class Solution:
    def largestAltitude(self, gain):

        current = 0
        maximum = 0

        for g in gain:

            # Update altitude
            current += g

            # Update maximum altitude
            maximum = max(maximum, current)

        return maximum