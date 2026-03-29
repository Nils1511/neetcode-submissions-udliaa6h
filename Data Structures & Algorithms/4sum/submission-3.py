class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            a = nums[i]
            
            for j in range(i+1, len(nums)-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                b = nums[j]

                l, r = j+1, len(nums) - 1

                while l<r:
                    tot_sum = a + b + nums[l] + nums[r]
                    
                    if tot_sum == target:
                        res.append([a, b, nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
                        while l<r and nums[r]==nums[r+1]:
                            r-=1
                    elif tot_sum > target:
                        r -= 1
                    else:
                        l += 1
        return res
                    

