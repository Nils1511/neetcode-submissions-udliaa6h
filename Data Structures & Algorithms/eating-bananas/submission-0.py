class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        res = high

        while low<=high:
            mid = (low+high)//2
            tot_time = 0
            for pile in piles:
                tot_time += (pile + mid - 1)//mid
            
            if tot_time <= h:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
            
        return res