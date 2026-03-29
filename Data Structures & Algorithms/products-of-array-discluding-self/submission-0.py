class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        countZero = 0
        for num in nums:
            if num == 0:
                countZero += 1
            else:
                product *= num 
        n = len(nums)
        if countZero >= 2:
            return [0] * n
        elif countZero == 1:
            result = [0] * n
            for i in range(n):
                if nums[i] == 0:
                    result[i] = int(product)
            return result
        else:
            result = []
            for num in nums: 
                result.append(int(product/num))
            return result