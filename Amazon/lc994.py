from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        n, m = len(grid), len(grid[0])
        queue = deque()
        oranges = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    oranges += 1
                elif grid[i][j] == 2:
                    queue.append([i, j])
        
        time = 0
        while queue:
            l = len(queue)
            for _ in range(l):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append([nx, ny])
                        oranges -= 1
            time += 1
        
        return max(0, time - 1) if oranges == 0 else -1