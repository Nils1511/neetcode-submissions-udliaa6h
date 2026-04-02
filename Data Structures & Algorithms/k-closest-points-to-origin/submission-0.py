class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
    
        for x, y in points:
            dist = x**2 + y**2
            min_heap.append((dist, [x, y]))
        
        # Transform list into a heap, O(n)
        heapq.heapify(min_heap)
        
        # Extract k smallest elements, O(k log n)
        result = []
        for _ in range(k):
            dist, point = heapq.heappop(min_heap)
            result.append(point)
            
        return result