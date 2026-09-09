import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for p in points:
            if len(heap) < k:
                x = (p[0] ** 2) + (p[1] ** 2)
                heapq.heappush_max(heap,(x,p))
            
            else:
                val, point = heap[0]
                x = (p[0] ** 2) + (p[1] ** 2)
                if x < val:
                    heapq.heappushpop_max(heap,(x,p))

        for _ in range(k):
            val, point = heapq.heappop_max(heap)
            res.append(point)

        return res

        

        