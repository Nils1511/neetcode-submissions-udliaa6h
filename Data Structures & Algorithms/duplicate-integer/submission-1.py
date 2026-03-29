class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        for num, count in freq_map.items():
            if count > 1:
                return True

        return False        