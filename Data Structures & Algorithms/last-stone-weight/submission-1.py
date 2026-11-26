class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        i = 0
        while i < len(stones)-1 :
            max1 = heapq.heappop_max(stones)
            max2 = heapq.heappop_max(stones)
            if max1 > max2:
                heapq.heappush_max(stones, max1-max2)
        stones.append(0)
        return stones[0]