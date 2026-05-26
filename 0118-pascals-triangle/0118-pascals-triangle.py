class Solution:
    def generate(self, numRows: int):
        
        triangle = []

        for i in range(numRows):

            # Create row with all 1s
            row = [1] * (i + 1)

            # Fill middle values
            for j in range(1, i):

                row[j] = triangle[i-1][j-1] + triangle[i-1][j]

            triangle.append(row)

        return triangle