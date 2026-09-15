class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        
        def memo(r,c, cache):
            if r >= m or c >= n or obstacleGrid[r][c] == 1:
                return 0

            if cache[r][c] > 0:
                return cache[r][c]

            if r == m - 1 and c == n - 1:
                return 1

            cache[r][c] = memo(r + 1, c, cache) + memo(r, c + 1, cache)

            return cache[r][c]

        return memo(0,0, [[0] * n for _ in range(m)])




        