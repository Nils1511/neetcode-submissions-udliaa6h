class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums_set = set(nums)
        # if len(nums_set) == len(nums):
        #     return False
        # return True

        freq = {}
        for num in nums:
            if num in freq:
                return True
            else:
                freq[num] = 1
        
        return False