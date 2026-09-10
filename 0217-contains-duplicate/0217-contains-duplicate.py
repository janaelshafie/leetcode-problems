class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hm = {}
        for n in nums:
            if n in hm:
                return True
            hm[n] = 1

        return False