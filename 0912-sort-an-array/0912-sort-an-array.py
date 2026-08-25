class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return self.mergeSort(nums, 0, len(nums) - 1)

    
    def mergeSort(self,nums, s, e):
        if (e - s) + 1 <= 1:
            return nums[s:e + 1]
        m = (s + e) // 2
        arr_l = self.mergeSort(nums, s, m)
        arr_r = self.mergeSort(nums, m + 1, e)

        return self.merge(arr_l, arr_r)

    def merge(self,arr_l, arr_r):
        nums = []
        i = 0
        j = 0
        while i < len(arr_l) and j < len(arr_r):
            if arr_l[i] <= arr_r[j]:
                nums.append(arr_l[i])
                i += 1
            else:
                nums.append(arr_r[j])
                j += 1
            
        nums.extend(arr_l[i:])
        nums.extend(arr_r[j:])

        return nums


        