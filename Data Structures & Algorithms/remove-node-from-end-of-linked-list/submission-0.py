# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverseLL(head: ListNode) -> ListNode:
            curr = head
            prev = None

            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        
        rev_head = reverseLL(head)
        # dummy = ListNode(0, rvsLL) # Use a dummy to handle deleting the first node easily
        # curr = dummy
        # cnt = 1
        if n == 1:
            new_rev_head = rev_head.next
            return reverseLL(new_rev_head)

        curr = rev_head
        for _ in range(n - 2): # Stop 1 node before the target
            curr = curr.next
        
        # 4. Delete the node
        if curr.next:
            curr.next = curr.next.next
            
        # 5. Reverse it back and return
        return reverseLL(rev_head)
                    