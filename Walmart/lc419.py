class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        def dfs(x, y):
            if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or board[x][y] == '.':
                return
            board[x][y] = '.'
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
        
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    count += 1
                    dfs(i, j)
        
        return count