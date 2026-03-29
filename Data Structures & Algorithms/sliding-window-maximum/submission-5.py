class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        leftmax = [0]*n
        rightmax = [0]*n

        leftmax[0] = nums[0]
        rightmax[n-1] = nums[n-1]
        for i in range(1, len(nums)):
            if i%k == 0:
                leftmax[i] = nums[i]
            else:
                leftmax[i] = max(leftmax[i-1], nums[i])

            if (n - 1 - i)%k == 0:
                rightmax[n-1-i] = nums[n-1-i]
            else:
                rightmax[n-1-i] = max(rightmax[n-i], nums[n-1-i])
        
        res = [0] * (n-k+1)
        for i in range(n-k+1):
            res[i] = max(leftmax[i+k-1], rightmax[i])
        
        return res