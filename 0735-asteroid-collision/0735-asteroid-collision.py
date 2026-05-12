class Solution:
    def asteroidCollision(self, asteroids):

        stack = []

        for asteroid in asteroids:

            alive = True

            # Collision possible
            while alive and asteroid < 0 and stack and stack[-1] > 0:

                # Top asteroid smaller
                if stack[-1] < abs(asteroid):

                    stack.pop()

                # Equal sizes
                elif stack[-1] == abs(asteroid):

                    stack.pop()
                    alive = False

                # Top asteroid bigger
                else:

                    alive = False

            # If asteroid survives
            if alive:
                stack.append(asteroid)

        return stack