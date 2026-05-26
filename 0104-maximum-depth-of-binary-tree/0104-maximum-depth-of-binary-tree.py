class Solution:
    def maxDepth(self, root):

        # Base case
        if not root:
            return 0

        # Depth of left subtree
        left = self.maxDepth(root.left)

        # Depth of right subtree
        right = self.maxDepth(root.right)

        # Return maximum depth
        return 1 + max(left, right)