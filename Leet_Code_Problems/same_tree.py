from typing import Optional


# 1. Define the Node structure
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 2. Your Solution Class
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res_p = []
        res_q = []

        def helper(node, res_list):
            if not node:
                res_list.append(None)
                return

            res_list.append(node.val)  # Record Root
            helper(node.left, res_list)  # Go Left
            helper(node.right, res_list)  # Go Right

        helper(p, res_p)
        helper(q, res_q)

        return res_p == res_q


# --- EXAMPLE FOR RUNNING IN PYCHARM ---
if __name__ == "__main__":
    # Let's create two identical trees:
    #      1
    #     / \
    #    2   3

    # Tree P
    tree_p = TreeNode(1)
    tree_p.left = TreeNode(2)
    tree_p.right = TreeNode(3)

    # Tree Q
    tree_q = TreeNode(1)
    tree_q.left = TreeNode(2)
    tree_q.right = TreeNode(3)

    # Initialize solution and test
    sol = Solution()
    result = sol.isSameTree(tree_p, tree_q)

    print(f"Are the trees the same? {result}")

    # Example of different trees
    tree_r = TreeNode(1, TreeNode(2), None)  # 2 is on the left
    tree_s = TreeNode(1, None, TreeNode(2))  # 2 is on the right

    print(f"Are trees R and S the same? {sol.isSameTree(tree_r, tree_s)}")