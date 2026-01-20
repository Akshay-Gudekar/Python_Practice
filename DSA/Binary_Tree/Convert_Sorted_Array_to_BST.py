from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Converts a sorted array to a height-balanced BST.
        """
        if not nums:
            return None

        # Find the middle index to ensure balance
        mid = len(nums) // 2

        # Create the root with the middle element
        root = TreeNode(nums[mid])

        # Recursively build the left and right subtrees
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root

def print_tree(node, level=0, prefix="Root: "):
    """
    Helper function to visualize the tree structure in the console.
    """
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.val))
        if node.left or node.right:
            print_tree(node.left, level + 1, "L--- ")
            print_tree(node.right, level + 1, "R--- ")


if __name__ == "__main__":
    sorted_nums = [-10, -3, 0, 5, 9]
    print(f"Input Array: {sorted_nums}\n")

    sol = Solution()
    bst_root = sol.sortedArrayToBST(sorted_nums)

    print("Resulting Height-Balanced BST Structure:")
    print_tree(bst_root)