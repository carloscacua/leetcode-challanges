from treenode import TreeNode

# Binary Tree Preorder Traversal
# Given a binary tree, return the preorder traversal of its nodes' values.
# iterative solution
def levelorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    result = []
    if root is None:
        return result
    s = [root]
    while s:
        current = []
        n = []
        for e in s:
            current.append(e.val)
            if e.left is not None:
                n.append(e.left)
            if e.right is not None:
                n.append(e.right)
        s = n
        result.append(current)

    return result
