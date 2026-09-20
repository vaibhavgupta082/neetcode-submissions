class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        mp = set()
        # Each row can contain digits 1–9 at most once.
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.' and board[i][j] in mp:
                    return False
                else:
                    mp.add(board[i][j])
            mp = set()

        # Each row can contain digits 1–9 at most once.
        for i in range(9):
            for j in range(9):
                if board[j][i] != '.' and board[j][i] in mp:
                    return False
                else:
                    mp.add(board[j][i])
            mp = set()

        # Each block can contain digits 1–9 at most once.
        for p in range(0,9,3):
            for k in range(0,9,3):
                for i in range(3):
                    for j in range(3):
                        if board[i+k][j+p] != '.' and board[i+k][j+p] in mp:
                            return False
                        else:
                            mp.add(board[i+k][j+p])
                mp = set()

        return True

            

        