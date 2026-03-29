class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # freq_map = {}
        # for num in nums:
        #     if num in freq_map:
        #         freq_map[num] += 1
        #     else:
        #         freq_map[num] = 1

        # for num, count in freq_map.items():
        #     if count > 1:
        #         return True

        # return False 

        num_set = set(nums)

        if len(nums) != len(num_set):
            return True

        return False       