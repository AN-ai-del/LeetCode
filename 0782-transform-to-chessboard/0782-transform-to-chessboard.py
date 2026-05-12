class Solution:
    def movesToChessboard(self, board):

        n = len(board)

        # Check validity
        for i in range(n):
            for j in range(n):

                if board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]:
                    return -1

        row_sum = sum(board[0])
        col_sum = sum(board[i][0] for i in range(n))

        row_swap = 0
        col_swap = 0

        # Count misplaced rows/cols
        for i in range(n):

            if board[i][0] == i % 2:
                row_swap += 1

            if board[0][i] == i % 2:
                col_swap += 1

        # Invalid counts
        if not (n // 2 <= row_sum <= (n + 1) // 2):
            return -1

        if not (n // 2 <= col_sum <= (n + 1) // 2):
            return -1

        # Even size
        if n % 2 == 0:

            row_swap = min(row_swap, n - row_swap)
            col_swap = min(col_swap, n - col_swap)

        # Odd size
        else:

            if row_swap % 2:
                row_swap = n - row_swap

            if col_swap % 2:
                col_swap = n - col_swap

        return (row_swap + col_swap) // 2