# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root, low, high):

        if not root:
            return 0

        # If value is smaller than low,
        # search only right subtree
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)

        # If value is greater than high,
        # search only left subtree
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)

        # Current node is in range
        return (
            root.val
            + self.rangeSumBST(root.left, low, high)
            + self.rangeSumBST(root.right, low, high)
        )