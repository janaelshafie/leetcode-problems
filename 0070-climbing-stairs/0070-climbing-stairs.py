class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dynp = [1,2]
        i = 3
        while i <= n:
            temp = dynp[1]
            dynp[1] = dynp[0] + dynp[1]
            dynp[0] = temp
            i += 1

        return dynp[1]
        