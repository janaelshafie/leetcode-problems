class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hmap = {}
        for s in strs:
            s_s = tuple(sorted(s))

            if s_s not in hmap:
                hmap[s_s] = []
    
            hmap[s_s].append(s)

        return list(hmap.values())
            


        