class ListNode:
    def __init__(self, key=-1, value=-1, next=None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:

    def __init__(self):
        self.buckets = [ListNode() for _ in range(10000)]

    def put(self, key: int, value: int) -> None:
        idx = key % len(self.buckets)
        chain = self.buckets[idx]
        while chain.next:
            if chain.next.key == key:
                chain.next.value = value
                return
            chain = chain.next
        chain.next = ListNode(key, value)

    def get(self, key: int) -> int:
        idx = key % len(self.buckets)
        chain = self.buckets[idx]
        while chain.next:
            if chain.next.key == key:
                return chain.next.value
            chain = chain.next
        return -1

    def remove(self, key: int) -> None:
        idx = key % len(self.buckets)
        chain = self.buckets[idx]
        while chain.next:
            if chain.next.key == key:
                chain.next = chain.next.next
                return
            chain = chain.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)