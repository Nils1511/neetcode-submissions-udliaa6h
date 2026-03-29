class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # [ -2, -1, 0, 1]
        n = len(nums)
        # n = 3
        for i in range(n):
            # while -2 < 1
            # while 1 >= 1 and nums[3] (1) != nums[0] (-2)
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                target_idx = nums[i] - 1 # nums[3] - 1
                # target_idx = 0
                # nums[3], nums[0] = nums[0], nums[3]
                nums[i], nums[target_idx] = nums[target_idx], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1