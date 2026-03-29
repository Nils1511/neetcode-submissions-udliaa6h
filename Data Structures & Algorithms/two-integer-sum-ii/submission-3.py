class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(len(numbers)):
        #     new_target = target - numbers[i]
        #     for j in range(i+1, len(numbers)):
        #         if numbers[j] == new_target:
        #             return [i+1, j+1]
        l = 0
        r = len(numbers) -1
        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum == target:
                return [l+1, r+1]
            elif curSum > target:
                r -= 1
            else:
                l += 1
