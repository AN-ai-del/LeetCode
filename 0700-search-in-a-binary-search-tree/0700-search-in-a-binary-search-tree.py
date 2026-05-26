class Solution:
    def searchBST(self, root, val):

        # If node doesn't exist
        if not root:
            return None

        # Found the value
        if root.val == val:
            return root

        # Search left subtree
        if val < root.val:
            return self.searchBST(root.left, val)

        # Search right subtree
        return self.searchBST(root.right, val)