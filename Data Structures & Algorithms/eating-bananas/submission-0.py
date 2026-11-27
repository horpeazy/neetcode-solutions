import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            mid = (l + r) // 2

            if self.checkEatingSpeed(piles, h, mid) == 0:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1

        return res

    def checkEatingSpeed(self, piles: List[int], h: int, k: int):
        total_hours = 0

        for pile in piles:
            total_hours += math.ceil(pile/k)

        if total_hours <= h:
            return 0
        
        return 1

        