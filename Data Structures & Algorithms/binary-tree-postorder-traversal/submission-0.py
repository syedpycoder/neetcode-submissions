# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        stack = [root]
        result = []
        if not root:
            return []


        while stack:

            current = stack.pop()
            result.append(current.val)

            if current.left:
                stack.append(current.left)

            if current.right:
                stack.append(current.right)

        return result[::-1]            
        