class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            totalHours = 0

            for pile in piles:
                totalHours += (pile + k - 1) // k

            if totalHours <= h:
                res = k
                r = k - 1

            else:
                l = k + 1

        return res


        