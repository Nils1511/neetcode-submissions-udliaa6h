class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for day, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp, in_day = stack.pop()
                out  = day - in_day
                res[in_day] = out
            stack.append([t, day])
        
        return res