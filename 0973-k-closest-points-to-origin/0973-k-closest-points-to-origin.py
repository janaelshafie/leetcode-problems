class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        self.quickSelect(points,k - 1,0,len(points) - 1)
        return points[:k]

    def quickSelect(self, points, k, s, e):
        left = s
        pivot_index = random.randint(s,e)
        points[pivot_index], points[e] = points[e], points[pivot_index]
        pivot = points[e]
        res_pivot = (points[e][0] - 0) ** 2 + (points[e][1] - 0) ** 2
        for i in range(s, e):
            if (points[i][0] - 0) ** 2 + (points[i][1] - 0) ** 2 <= res_pivot:
                temp = points[left]
                points[left] = points[i]
                points[i] = temp
                left += 1

        points[e] = points[left]
        points[left] = pivot

        if k == left:
            return points

        elif k < left:
            return self.quickSelect(points,k,s,left - 1)

        else:
            return self.quickSelect(points,k,left + 1,e)
        



        