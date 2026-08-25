class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        self.mergeSort(nums, 0, len(nums) - 1)

        return nums[k - 1]

    def mergeSort(self, nums, s, e):

        if s >= e:
            return

        m = (s + e) // 2

        self.mergeSort(nums, s, m)
        self.mergeSort(nums, m + 1, e)
        self.merge(nums, s, m, e)

        return nums

    def merge(self, nums, s, m, e):
        temp = []
        i = s
        j = m + 1
        while i <= m and j <= e:
            if nums[i] >= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1

        temp.extend(nums[j: e + 1])
        temp.extend(nums[i:m + 1])

        nums[s: e + 1] = temp
        return nums
        