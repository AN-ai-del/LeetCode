class Solution:
    def maxPathSum(self, root):

        self.ans = float('-inf')

        def dfs(node):

            if not node:
                return 0

            # Best gain from left subtree
            left = max(0, dfs(node.left))

            # Best gain from right subtree
            right = max(0, dfs(node.right))

            # Path passing through current node
            current_sum = node.val + left + right

            # Update answer
            self.ans = max(self.ans, current_sum)

            # Return best single path upward
            return node.val + max(left, right)

        dfs(root)

        return self.ans