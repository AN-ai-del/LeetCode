class Solution:
    def getRow(self, rowIndex: int):

        row = [1]

        for i in range(1, rowIndex + 1):

            # Add new 1 at end
            row.append(1)

            # Update middle values from right to left
            for j in range(i - 1, 0, -1):

                row[j] = row[j] + row[j - 1]

        return row