class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        data = []
        for i in range(len(position)):
            data.append([position[i], speed[i]])
        
        data.sort(reverse = True)

        time_stack = []
        for p, s in data:
            time = (target - p) / s
            time_stack.append(time)
            if len(time_stack) >= 2 and time_stack[-1] <= time_stack[-2]:
                time_stack.pop()
        return len(time_stack)
        
