class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        amt = 0
        leftMax, rightMax = height[l], height[r]

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                amt += leftMax - height[l]

            else: 
                r -= 1
                rightMax = max(rightMax, height[r])
                amt += rightMax - height[r]

        return amt