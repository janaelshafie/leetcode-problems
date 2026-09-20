class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hmap = {}
        # for s in strs:
        #     key = "".join(sorted(s))

        #     if key not in hmap:
        #         hmap[key] = []
    
        #     hmap[key].append(s)

        # return list(hmap.values())

        #or instead of sorting we could do a frequency counting

        for s in strs:
            count = [0] * 26

            for char in s:
                count[ord(char) - ord("a")] += 1

            key = tuple(count)

            if key not in hmap:
                hmap[key] = []

            hmap[key].append(s)

        return list(hmap.values())
            


        