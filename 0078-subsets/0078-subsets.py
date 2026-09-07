class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sbst = []
        def dfs(index):
            if index >= len(nums):
                res.append(sbst.copy())
                return

            #include nums[index]
            sbst.append(nums[index])
            dfs(index + 1)

            #dont include nums[index]
            sbst.pop()
            dfs(index + 1)
        
        dfs(0)

        return res
        