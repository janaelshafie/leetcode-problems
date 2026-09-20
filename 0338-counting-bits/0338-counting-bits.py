class Solution:
    def countBits(self, n: int) -> list[int]:
        res = [0] * (n + 1)

        for i in range(len(res)):
            k = i
            while k > 0:
                if k & 1 == 1:
                    res[i] += 1
                k = k >> 1

        return res

        