class Solution:
    def getMinimumDifference(self, root):

        self.prev = None
        self.ans = float('inf')

        def inorder(node):

            if not node:
                return

            # Left subtree
            inorder(node.left)

            # Current node
            if self.prev is not None:

                self.ans = min(
                    self.ans,
                    node.val - self.prev
                )

            self.prev = node.val

            # Right subtree
            inorder(node.right)

        inorder(root)

        return self.ans