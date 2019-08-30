from treenode import TreeNode

# Path Sum
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all
# the values along the path equals the given sum.
# iterative solution
def hasPathSum(root, sum):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if root is None:
        return sum == 0
    s = [root]
    while s:
        node = s.pop()
        if node.right is None and node.left is None and node.val == sum:
            return True
        if node.right is not None:
            node.right.val += node.val
            s.append(node.right)
        if node.left is not None:
            node.left.val += node.val
            s.append(node.left)

    return False
