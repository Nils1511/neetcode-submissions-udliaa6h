class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ex = set(nums)
        sequence_starter = []
        for num in ex:
            if num - 1 not in ex:
                sequence_starter.append(num)
            

        ans = 0
        for start in sequence_starter:
            count = 1
            curr = start
            while curr + 1 in ex:
                count += 1
                curr += 1
                start = start + 1
            ans = max(ans, count)

        return ans
            