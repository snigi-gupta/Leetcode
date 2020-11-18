# https://leetcode.com/problems/path-sum/
# https://www.youtube.com/watch?v=Hg82DzMemMI


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root, _sum):
        if not root:
            return False
        elif not root.left and not root.right and _sum - root.val == 0:
            return True
        else:
            return self.hasPathSum(root.left, _sum - root.val) or self.hasPathSum(root.right, _sum - root.val)


if __name__ == "__main__":

    """
            5
        4       8
    11        13    4
7       2               1
    """
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right = TreeNode(8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(4)

    obj = Solution()
    print(obj.hasPathSum(root, 22))

