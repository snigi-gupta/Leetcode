# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# https://www.youtube.com/watch?v=to2XMEXE1ms

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self.maxDepth(node.left), self.maxDepth(node.right))

    def iterative(self, node):
        stack = []
        if node is not None:
            stack.append((1, node))

        depth = 0
        while stack:
            curr_depth, curr_node = stack.pop()
            if curr_node is not None:
                depth = max(depth, curr_depth)
                stack.append((1 + curr_depth, curr_node.left))
                stack.append((1 + curr_depth, curr_node.right))
        return depth


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(2)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(6)
    root.right.left.right = TreeNode(8)

    obj = Solution()
    print(obj.maxDepth(root))
    print(obj.iterative(root))