class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        maximum = arr[-1]
        for i in range(len(arr) - 2, -1, -1):
            current = arr[i]
            arr[i] = maximum
            maximum = max(maximum,current)
        arr[-1] = -1
        return arr



        