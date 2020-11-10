# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Pre-order traversal
    def printTree(self, root):
        print(root.val, end=" ")
        if root.left:
            self.printTree(root.left)
        # print(' ' * 4 * lev + '->', root.val)

        if root.right:
            self.printTree(root.right)
        return result

    """
        Don't know why this is worng.
    def insertLeaf(self, root, leaf):
        if root.val > leaf:
            if root.left is None:
                root.left = TreeNode(leaf)
            else:
                self.insertLeaf(root.left, leaf)
        elif root.val < leaf:
            if root.right is None:
                root.right = TreeNode(leaf)
            else:
                self.insertLeaf(root.right, leaf)
        else:
            root.val = leaf
        return root

    def sortedArrayToBST(self, nums):
        if len(nums)<1:
            return
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        for num in nums:
            self.insertLeaf(root, num)

        print(self.printTree(root, result=[]))
    """
    def sortedArrayToBST(self, nums):
        def helper(left, right):
            if left >= right:
                return None

            mid = left + ((right - left) // 2)
            root = TreeNode(nums[mid])
            root.left = helper(left, mid)
            root.right = helper(mid+1, right)

            return root

        return helper(0, len(nums))


if __name__ == "__main__":
    obj = Solution()
    # obj.sortedArrayToBST(nums=[-10, -3, 0, 5, 9])
    result = obj.sortedArrayToBST(nums=[0,1,2,3,4,5])
    obj.printTree(result)