class Solution:
    def canIEatItAll(self, k, piles, h):
        hours_needed = sum(math.ceil(pile / k) for pile in piles)
        if hours_needed > h:
            return -1
        else:
            return 1
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = 0
        while low <= high:
            mid = (low+high)//2
            if self.canIEatItAll(mid, piles, h) == -1:
                low = mid+1
            else:
                ans = mid
                high = mid - 1
        return ans