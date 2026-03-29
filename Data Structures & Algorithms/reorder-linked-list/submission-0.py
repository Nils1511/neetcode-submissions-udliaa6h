# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
    
        # 1. Store the ACTUAL node objects in an array
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

            
        l, r = 0, len(nodes) - 1
        while l < r:
            # Connect the left node to the right node
            nodes[l].next = nodes[r]
            l += 1
            
            # Check if pointers met; if so, break early to avoid cycles
            if l >= r:
                break
                
            # Connect the right node to the next left node
            nodes[r].next = nodes[l]
            r -= 1

        # 3. CRITICAL: Set the next of the last node to None to terminate the list
        nodes[l].next = None