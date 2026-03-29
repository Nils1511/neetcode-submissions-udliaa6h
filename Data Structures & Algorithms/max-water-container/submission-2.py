class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights) - 1
        maxi = 0
        while l<r:
            h = min(heights[l], heights[r])
            area = (r - l)*h
            maxi = max(area, maxi)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxi