class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}
        def memo(i,j, dp):
            if i == len(text1) or j == len(text2):
                return 0

            if (i,j) in dp:
                return dp[(i,j)]

            if text1[i] == text2[j]:
                dp[(i,j)] = 1 + memo(i + 1, j + 1, dp)

            else:
                dp[(i,j)] = max(memo(i + 1, j, dp), memo(i, j + 1, dp))

            return dp[(i,j)]

        return memo(0, 0, dp)

        


            

            

        