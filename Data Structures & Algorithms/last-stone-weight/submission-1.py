class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # 1. Transform to max-heap (by negating)
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)  # O(n) time

        while len(max_heap) > 1:
            # 3. Get the maximum element
            x = -heapq.heappop(max_heap)  # Returns 50
            y = -heapq.heappop(max_heap)
            if x == y:
                continue
            heapq.heappush(max_heap, -(x-y))

        return -heapq.heappop(max_heap) if len(max_heap) == 1 else 0