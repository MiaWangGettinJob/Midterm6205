from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

class Solution:
    def travers(self, root):
        def helper(root):
            if not root:
                return
            if root.left:
                root.left.parent = root
                helper(root.left)
            if root.right:
                root.right.parent = root
                helper(root.right)
        helper(root)

def main():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    a = Solution
    a.travers(a, root)
    print(root.right.left.parent.val)


main()