class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def memo(r, c, cache):
            if r >= m or c >= n:
                return 0

            if r == m - 1 and c == n - 1:
                return 1

            if cache[r][c] > 0:
                return cache[r][c]

            cache[r][c] = memo(r + 1, c, cache) + memo(r, c + 1, cache)

            return cache[r][c]

        return memo(0, 0, [[0] * n for _ in range(m)])

        