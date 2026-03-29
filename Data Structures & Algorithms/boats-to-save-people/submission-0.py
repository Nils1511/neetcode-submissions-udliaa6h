class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        numBoats = 0
        people.sort()
        l = 0
        r = len(people) - 1
        while l <= r:
            if people[r] >= limit:
                numBoats += 1
                r -= 1
            elif people[r] + people[l] <= limit:
                numBoats += 1
                l += 1
                r -= 1
            elif people[r] + people[l] > limit:
                numBoats += 1
                r -= 1
        
        return numBoats