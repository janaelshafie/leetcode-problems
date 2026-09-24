class Solution:
    def findMin(self, nums: list[int]) -> int:
        s = 0
        e = len(nums) - 1
            
        while s < e:
            ip = (e + s) // 2

            if nums[ip] < nums[e]:
                e = ip

            else:
                s = ip + 1

        return nums[s]

        