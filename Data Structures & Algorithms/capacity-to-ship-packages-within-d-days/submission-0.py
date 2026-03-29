class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
 
        l = max(weights)
        r = sum(weights)
        res = r
        while l <= r:
            cap = (l+r)//2
            take = 1
            temp = 0
            for weight in weights:
                if temp + weight > cap:
                    take += 1
                    temp = 0
                temp += weight
            
            if take <= days:
                res = cap
                r = cap - 1
            else:
                l = cap + 1
        
        return res