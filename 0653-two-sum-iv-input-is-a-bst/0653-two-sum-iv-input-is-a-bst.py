class Solution:
    def findTarget(self, root, k):

        seen = set()

        def dfs(node):

            if not node:
                return False

            # Check complement
            if (k - node.val) in seen:
                return True

            # Store current value
            seen.add(node.val)

            # Search left or right
            return dfs(node.left) or dfs(node.right)

        return dfs(root)