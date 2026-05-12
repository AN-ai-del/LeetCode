class Solution:
    def pushDominoes(self, dominoes: str) -> str:

        s = list(dominoes)

        n = len(s)

        forces = []

        # Store positions of L and R
        for i, ch in enumerate(s):

            if ch != '.':
                forces.append((i, ch))

        # Add virtual boundaries
        forces = [(-1, 'L')] + forces + [(n, 'R')]

        # Process between forces
        for k in range(len(forces) - 1):

            i, left = forces[k]
            j, right = forces[k + 1]

            # Same directions
            if left == right:

                for x in range(i + 1, j):
                    s[x] = left

            # Opposite directions moving inward
            elif left == 'R' and right == 'L':

                l = i + 1
                r = j - 1

                while l < r:
                    s[l] = 'R'
                    s[r] = 'L'

                    l += 1
                    r -= 1

        return "".join(s)