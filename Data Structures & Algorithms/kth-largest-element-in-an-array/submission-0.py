class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # max_heap = [-x for x in nums]
        # while k > 1:
        #     heapq.heapify(max_heap)
        #     heapq.heappop(max_heap)
        # heapq.heapify(max_heap)
        # return -heapq.heappop(max_heap)

        res = heapq.nlargest(k, nums)
        return res[-1]