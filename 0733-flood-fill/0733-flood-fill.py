class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        scc = image[sr][sc]
        def dfs(sr, sc, color):
            ROWS, COLS = len(image), len(image[0])

            if scc == color:
                return

            if (min(sr,sc) < 0 or
            sr == ROWS or sc == COLS or 
            image[sr][sc]!= scc):
                return

            image[sr][sc] = color

            dfs(sr + 1, sc, color)
            dfs(sr - 1, sc, color)
            dfs(sr, sc + 1, color)
            dfs(sr, sc - 1, color)

            return

        dfs(sr, sc, color)

        return image
    
        