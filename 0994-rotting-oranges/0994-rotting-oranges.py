from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        minutes = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        neighbours = [[1,0],[-1,0],[0,1],[0,-1]]
        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                for dr, dc in neighbours:
                    nr = r + dr
                    nc = c + dc

                    if (min(nr,nc) < 0 or nr >= ROWS or nc >= COLS or
                        grid[nr][nc] == 0 or grid[nr][nc] == 2):
                        continue

                    queue.append((nr,nc))
                    grid[nr][nc] = 2
                    fresh -= 1
            
            if queue:
                minutes += 1

        
        return -1 if fresh > 0 else minutes

        