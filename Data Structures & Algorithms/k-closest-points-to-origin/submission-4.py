class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = [(p[0]**2 + p[1]**2, [p[0], p[1]]) for p in points]
        heapq.heapify(distance)
        ans = []
        for i in range(0,k):
            x, point = heapq.heappop(distance)
            ans.append(point)
        return ans