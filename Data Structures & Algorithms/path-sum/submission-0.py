# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        pathsum = 0
        if not root:
            return False
        
        def pathSum(root, pathsum, targetsum):
            pathsum += root.val
            
            
            if root.left or root.right:
                if root.left and pathSum(root.left, pathsum, targetsum):
                    return True
                if root.right and pathSum(root.right, pathsum, targetsum):
                    return True
            else:
                return pathsum == targetsum
            pathsum -= root.val
            return False
        return pathSum(root, pathsum, targetSum)