class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[-k%len(nums):] + nums [:-k%len(nums)]
        # k %= len(nums)
        # while k>0:
        #     temp = nums[0]
        #     nums[0] = nums[len(nums)-1]
        #     for j in range(1, len(nums)):
        #         temp1 = nums[j]
        #         nums[j] = temp
        #         temp = temp1
        #     k -= 1
