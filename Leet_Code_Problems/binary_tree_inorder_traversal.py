# 1. Define what a "Node" looks like
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 2. Our Inorder Traversal Function
def inorderTraversal(root):
    res = []

    def helper(node):
        if not node:
            return
        helper(node.left)  # Go Left
        res.append(node.val)  # Record Root
        helper(node.right)  # Go Right

    helper(root)
    return res


# 3. The "Driver" code to test it
if __name__ == "__main__":
    # Let's manually build this tree:
    #      1
    #       \
    #        2
    #       /
    #      3

    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    # Run the function
    print("Inorder Traversal Result:")
    print(inorderTraversal(root))