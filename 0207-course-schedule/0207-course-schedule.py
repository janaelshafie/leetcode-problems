class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) <= 1:
            return True

        map = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            map[crs].append(pre)

        visiting = set()

        def dfs(crs):

            if crs in visiting:
                return False

            if map[crs] == []:
                return True

            visiting.add(crs)

            for pre in map[crs]:
                if not dfs(pre):
                    return False
                
            visiting.remove(crs)
            map[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True
            
        