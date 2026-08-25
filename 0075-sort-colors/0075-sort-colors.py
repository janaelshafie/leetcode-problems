class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        counts = [0,0,0]

        for n in nums:
            counts[n] += 1
        
        i = 0
        k = 0
        for k in range(3):
            for _ in range(counts[k]):
                nums[i] = k
                i += 1
            k += 1
        
        return nums

        