class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(9):
            rowset = set()
            for j in range(9):
                if board[i][j] in rowset:
                    return False
                if board[i][j] != '.':
                    rowset.add(board[i][j])
        
        for i in range(9):
            colset = set()
            for j in range(9):
                if board[j][i] in colset:
                    return False
                if board[j][i] != '.':
                    colset.add(board[j][i])
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                matset = set()
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        if board[x][y] in matset:
                            return False
                        if board[x][y] != '.':
                            matset.add(board[x][y])
        
        return True