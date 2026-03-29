class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_set = set(nums)

        target = 1
        while True:
            if target not in num_set:
                return target
            target += 1

        
        
