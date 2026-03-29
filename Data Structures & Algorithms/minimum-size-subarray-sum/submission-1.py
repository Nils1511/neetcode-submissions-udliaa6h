class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        min_length = float('inf')
        sum = 0
        while right < len(nums):
            sum += nums[right]
            while sum >= target:
                min_length = min(min_length, right - left + 1)
                sum -= nums[left]
                left += 1
            right += 1
        return min_length if not min_length == float('inf') else 0