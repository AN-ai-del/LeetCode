class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # incoming[i] = how many people trust i
        incoming = [0] * (n + 1)

        # outgoing[i] = how many people i trusts
        outgoing = [0] * (n + 1)

        # Check every trust relationship
        for a, b in trust:

            # a trusts someone
            outgoing[a] += 1

            # b is trusted by someone
            incoming[b] += 1

        # Find the judge
        for i in range(1, n + 1):

            # Trusted by everyone and trusts nobody
            if incoming[i] == n - 1 and outgoing[i] == 0:
                return i

        return -1
        