class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matx = [[0 for _ in range(n)] for _ in range(m)]
        # print (matx)
        for i in indices:
            col = i[1]
            row = i[0]
            for c in range(n):
                matx[row][c] += 1
                # print(matx)
            for r in range(len(matx)):
                matx[r][col] += 1
                # print(matx)
        count = 0
        # print(matx)
        for r in matx:
            # print(r)
            for e in r:
                # print(e)
                if e%2 != 0:
                    count += 1
        # print(count)
        return count