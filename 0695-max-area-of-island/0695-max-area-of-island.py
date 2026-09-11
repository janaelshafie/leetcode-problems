class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        self.max_area = 0
        self.icount = 0
        def dfs(r,c):
            if (min(r,c) < 0 or r == ROWS or c == COLS or 
                grid[r][c] == 0):
                return 0

            grid[r][c] = 0
            self.icount += 1
            self.max_area = max(self.icount, self.max_area)

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                self.icount = 0
                if grid[r][c] == 1:
                    dfs(r,c)
                    

        return self.max_area


        