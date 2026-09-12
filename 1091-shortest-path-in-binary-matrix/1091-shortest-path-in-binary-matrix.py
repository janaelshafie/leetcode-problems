from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        queue = deque()
        visit = set()
        length = 0
        if grid[0][0] == 0:
            queue.append((0,0))
            visit.add((0,0))
            length += 1

        neighbours = [[1,0], [-1,0], [0,1], [0,-1], [1,1], [-1,-1], [1,-1], [-1,1]]

        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return length

                for dr, dc in neighbours:
                    nr = r + dr
                    nc = c + dc

                    if (min(nr,nc) < 0 or nr >= ROWS or nc >= COLS 
                        or (nr,nc) in visit or grid[nr][nc] == 1):
                        continue

                    queue.append((nr,nc))
                    visit.add((nr,nc))

            length += 1

        return -1





        