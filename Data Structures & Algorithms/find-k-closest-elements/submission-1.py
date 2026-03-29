class Solution:
    def findClosestElements(self, nums: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(nums) - 1

        while right - left + 1 > k:
            if abs(nums[left] - x) > abs(nums[right] - x):
                left += 1
            else:
                right -= 1
        return nums[left:right+1]