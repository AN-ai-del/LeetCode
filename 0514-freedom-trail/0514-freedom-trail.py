from collections import defaultdict
from functools import lru_cache

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:

        n = len(ring)

        # Store all positions of every character
        positions = defaultdict(list)

        for i, ch in enumerate(ring):
            positions[ch].append(i)

        @lru_cache(None)
        def dfs(ring_pos, key_index):

            # All characters completed
            if key_index == len(key):
                return 0

            target = key[key_index]

            ans = float('inf')

            # Try every occurrence of target char
            for pos in positions[target]:

                # Clockwise / anticlockwise distance
                diff = abs(pos - ring_pos)

                steps = min(diff, n - diff)

                # +1 for pressing button
                total = steps + 1 + dfs(pos, key_index + 1)

                ans = min(ans, total)

            return ans

        return dfs(0, 0)