class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i):
            if i == len(nums):
                res.append(nums.copy())
                return
            
            
            used = set()
            for j in range(i, len(nums)):
                if nums[j] in used:
                    continue
                used.add(nums[j])
                nums[i], nums[j] = nums[j], nums[i]
                dfs(i+1)
                nums[i], nums[j] = nums[j] , nums[i]

        nums.sort()  
        dfs(0)
        return res