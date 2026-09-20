class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hmap = {}
        for s in strs:
            key = "".join(sorted(s))

            if key not in hmap:
                hmap[key] = []
    
            hmap[key].append(s)

        return list(hmap.values())
            


        