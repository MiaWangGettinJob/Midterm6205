#Time complexity O(N)
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None, nextLeft = None):
        self.val = val
        self.left = left
        self.right = right
        self.nextLeft = nextLeft

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        result = []
        if not root:
            return root
        queue = deque()
        queue.append(root)
        while queue:
            length = len(queue)
            for i in range(length):
                current = queue.popleft()
                if i != length - 1:
                    queue[0].nextLeft = current
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
        return root

def main():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    a = Solution
    a.connect(a, root)
    print(root.right.right.nextLeft.val)


main()
