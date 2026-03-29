# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def height(root):
            if not root:
                return 0
            left = height(root.left)
            right = height(root.right)
        
            return 1 + max(left, right)

        leftsub = height(root.left)
        rightsub = height(root.right)

        if abs(leftsub - rightsub) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
            