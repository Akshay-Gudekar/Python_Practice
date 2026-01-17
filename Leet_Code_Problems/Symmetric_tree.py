from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.isMirror(root.left, root.right)

    def isMirror(self, t1, t2):
        # If both are null, they match
        if not t1 and not t2:
            return True
        # If only one is null, they don't match
        if not t1 or not t2:
            return False

        # 1. Values must match
        # 2. t1's left must match t2's right (Outer edges)
        # 3. t1's right must match t2's left (Inner edges)
        return (t1.val == t2.val) and \
            self.isMirror(t1.left, t2.right) and \
            self.isMirror(t1.right, t2.left)


# --- EXAMPLE FOR PYCHARM ---
if __name__ == "__main__":
    # Create a Symmetric Tree:
    #      1
    #     / \
    #    2   2
    #   / \ / \
    #  3  4 4  3

    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(3), TreeNode(4))
    root.right = TreeNode(2, TreeNode(4), TreeNode(3))

    sol = Solution()
    print(f"Is tree symmetric? {sol.isSymmetric(root)}")  # Output: True

    # Create an Asymmetric Tree:
    #      1
    #     / \
    #    2   2
    #     \   \
    #      3   3
    root2 = TreeNode(1)
    root2.left = TreeNode(2, None, TreeNode(3))
    root2.right = TreeNode(2, None, TreeNode(3))

    print(f"Is tree 2 symmetric? {sol.isSymmetric(root2)}")  # Output: False