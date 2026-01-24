# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        # Step 1: Handle an empty tree
        if not root:
            return False

        # Step 2: Check if current node is a leaf
        # A leaf has no left or right children
        if not root.left and not root.right:
            return targetSum == root.val

        # Step 3: Recurse down. We subtract the current node's value
        # from the targetSum to see what's left for the children.
        remaining_sum = targetSum - root.val

        # We return True if a path exists in EITHER the left or right subtree
        return self.hasPathSum(root.left, remaining_sum) or \
            self.hasPathSum(root.right, remaining_sum)


# --- Code to test it in PyCharm ---
if __name__ == "__main__":
    # Let's build a small tree:
    #      5
    #     / \
    #    4   8
    #   /
    #  11

    node11 = TreeNode(11)
    node4 = TreeNode(4, left=node11)
    node8 = TreeNode(8)
    root_node = TreeNode(5, left=node4, right=node8)

    sol = Solution()

    # Test case 1: Path 5 -> 4 -> 11 (Sum = 20)
    print(f"Path sum 20 exists: {sol.hasPathSum(root_node, 20)}")  # True

    # Test case 2: Path sum that doesn't exist
    print(f"Path sum 5 exists: {sol.hasPathSum(root_node, 5)}")  # False (5 is not a leaf)