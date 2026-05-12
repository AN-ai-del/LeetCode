class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:

        result = []

        while a > 0 or b > 0:

            # Check last two characters
            if len(result) >= 2 and result[-1] == result[-2]:

                # If last two are same,
                # force opposite character

                if result[-1] == 'a':

                    result.append('b')
                    b -= 1

                else:

                    result.append('a')
                    a -= 1

            else:

                # Otherwise place character
                # with larger remaining count

                if a >= b and a > 0:

                    result.append('a')
                    a -= 1

                elif b > 0:

                    result.append('b')
                    b -= 1

        return "".join(result)