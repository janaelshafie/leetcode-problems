class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        scc = image[sr][sc]
        self.image = image
        def dfs(sr, sc, color):
            ROWS, COLS = len(self.image), len(self.image[0])

            if (min(sr,sc) < 0 or
            sr == ROWS or sc == COLS or 
            self.image[sr][sc]!= scc or self.image[sr][sc] == color):
                return

            self.image[sr][sc] = color

            dfs(sr + 1, sc, color)
            dfs(sr - 1, sc, color)
            dfs(sr, sc + 1, color)
            dfs(sr, sc - 1, color)

            return

        dfs(sr, sc, color)

        return self.image
    
        