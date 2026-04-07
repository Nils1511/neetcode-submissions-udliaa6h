class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        frequency_map = {}
        for num in nums:
                frequency_map[num] = 1 + frequency_map.get(num, 0)
        
        result = []
        for num, freq in frequency_map.items():
            if freq > n/3:
                result.append(num)

        return result

        