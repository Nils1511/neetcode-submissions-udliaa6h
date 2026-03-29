class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # if nums[0] > 0:
        #     return []
        # i, k = 0, len(nums) - 1
        res = []
        for i in range(len(nums) -2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            if nums[i]>0:
                break
            a = nums[i]
            l, r = i+1, len(nums) -1
            while l < r:
                sum = a + nums[l] + nums[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    # Skip duplicates for the second and third elements
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
           
        return res 