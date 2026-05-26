class Solution:
    def kthSmallest(self, root, k):

        self.k = k
        self.ans = -1

        def inorder(node):

            if not node:
                return

            # Left
            inorder(node.left)

            # Visit current node
            self.k -= 1

            if self.k == 0:
                self.ans = node.val
                return

            # Right
            inorder(node.right)

        inorder(root)

        return self.ans