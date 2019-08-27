from treenode import TreeNode


# Binary Tree Preorder Traversal
# Given a binary tree, return the preorder traversal of its nodes' values.
# iterative solution
def postorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    result = []
    if root is None:
        return result
    s = [root]
    while s:
        node = s.pop()
        if type(node) == int:
            result.append(node)
        else:
            s.append(node.val)
            if node.right is not None:
                s.append(node.right)
            if node.left is not None:
                s.append(node.left)
    return result