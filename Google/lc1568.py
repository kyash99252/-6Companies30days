class Solution:
    def __init__(self):
        self.directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    def minDays(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(row, col, visit):
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == 0 or (row, col) in visit:
                return
            visit.add((row, col))
            for dx, dy in self.directions:
                nrow, ncol = row + dx, col + dy
                dfs(nrow, ncol, visit)

        def count_islands():
            visit = set()
            count = 0
            for row in range(rows):
                for col in range(cols):
                    if grid[row][col] and (row, col) not in visit:
                        dfs(row, col, visit)
                        count += 1
            return count

        if count_islands() != 1:
            return 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    grid[row][col] = 0
                    if count_islands() != 1:
                        return 1
                    grid[row][col] = 1
        return 2