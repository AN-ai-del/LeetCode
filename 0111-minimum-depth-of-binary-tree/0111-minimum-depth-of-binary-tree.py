class Solution:
    def minDepth(self, root):
        
        # Empty tree
        if not root:
            return 0

        # If left child does not exist
        if not root.left:
            return 1 + self.minDepth(root.right)

        # If right child does not exist
        if not root.right:
            return 1 + self.minDepth(root.left)

        # Both children exist
        return 1 + min(
            self.minDepth(root.left),
            self.minDepth(root.right)
        )