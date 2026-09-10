class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hm = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in hm:
                return [hm[x], i]
            hm[target - x] = i