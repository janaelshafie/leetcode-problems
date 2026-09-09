import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        i = 0
        while len(heap) < k:
            x = (points[i][0] ** 2) + (points[i][1] ** 2)
            heap.append((x,points[i]))
            i += 1

        heapq.heapify_max(heap)

        while i < len(points):
            val, point = heap[0]
            x = (points[i][0] ** 2) + (points[i][1] ** 2)
            if x < val:
                heapq.heappushpop_max(heap,(x,points[i]))
            i += 1

        while k > 0:
            val, point = heapq.heappop_max(heap)
            res.append(point)
            k -= 1

        return res

        

        