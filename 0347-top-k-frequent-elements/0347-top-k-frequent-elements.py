class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hmap = {}
        res = []
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            if n not in hmap:
                hmap[n] = 0

            hmap[n] += 1

        for num, cnt in hmap.items():
            freq[cnt].append(num)

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)

            if len(res) == k:
                return res




        

        




        