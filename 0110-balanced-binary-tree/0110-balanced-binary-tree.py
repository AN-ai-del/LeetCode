class Solution:
    def isBalanced(self, root):

        def height(node):

            # Empty tree
            if not node:
                return 0

            # Left subtree height
            left = height(node.left)

            # If already unbalanced
            if left == -1:
                return -1

            # Right subtree height
            right = height(node.right)

            # If already unbalanced
            if right == -1:
                return -1

            # Check balance condition
            if abs(left - right) > 1:
                return -1

            # Return height
            return 1 + max(left, right)

        return height(root) != -1