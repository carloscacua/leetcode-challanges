from treenode import TreeNode


def isMirror(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is not None and root2 is not None:
        return root1.val == root2.val and isMirror(root1.left, root2.right) and isMirror(root1.right, root2.left)

    return False


# Symmetric Tree
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
def isSymmetric(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    return isMirror(root, root)
