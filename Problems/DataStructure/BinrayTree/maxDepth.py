from treenode import TreeNode


# Binary Tree Preorder Traversal
# Given a binary tree, return the preorder traversal of its nodes' values.
# iterative solution
def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if root is None:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))
