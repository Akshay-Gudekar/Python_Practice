from typing import Optional


# 1. Define the Tree Node structure
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1


# 2. Let's test it!
if __name__ == "__main__":
    # We will manually build this tree:
    #      3
    #     / \
    #    9  20

    node_9 = TreeNode(9)
    node_20 = TreeNode(20)
    root_node = TreeNode(3, node_9, node_20)

    # 3. Initialize the solution and print the result
    sol = Solution()
    print(f"The maximum depth of the tree is: {sol.maxDepth(root_node)}")