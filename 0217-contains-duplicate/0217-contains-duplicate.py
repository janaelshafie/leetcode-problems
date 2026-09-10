class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hm = {}
        for n in nums:
            if n not in hm:
                hm[n] = 1
            else:
                return True

        return False
        