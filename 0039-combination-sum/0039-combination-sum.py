class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sum_sbst = []

        def dfs(i , remainder):
            if remainder == 0:
                res.append(sum_sbst.copy())
                return

            if i >= len(candidates):
                return

            if remainder - candidates[i] >= 0:
                sum_sbst.append(candidates[i])
                dfs(i, remainder - candidates[i])
                sum_sbst.pop()
            
            dfs(i + 1, remainder)

        dfs(0, target)
        return res

        