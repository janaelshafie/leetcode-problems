class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0],nums[1])

        def dp(i):            
            if i > len(nums) - 1:
                return 0

            if i in cache:
                return cache[i]

            opt1 = nums[i] + dp(i + 2)
            opt2 = dp(i + 1)

            cache[i] = max(opt1, opt2)

            return cache[i]

        return dp(0)
        