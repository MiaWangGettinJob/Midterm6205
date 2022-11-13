#Time Comlexity: worst case O(N)

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def helper(self, root, low, high):
        result = []
        def Range(root, low, high):
            nonlocal result
            if low <= root.val <= high:
                result.append(root.val)
                print(root.val)
            if root.val >= low and root.left:
                Range(root.left, low, high)
            if root.val <= high and root.right:
                Range(root.right, low, high)

        Range(root, low, high)
        print(result)




def main():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    a = Solution

    print(a.helper(a, root, 10, 20))


main()
