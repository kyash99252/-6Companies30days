# Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.pc = {}

    def populatePC(self, node: Optional[TreeNode]) -> None:
        if node.left:
            self.pc[node.left] = node
            self.populatePC(node.left)
        if node.right:
            self.pc[node.right] = node
            self.populatePC(node.right)
    
    def findNode(self, node: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not node:
            return None
        elif node.val == target:
            return node
        else:
            left = self.findNode(node.left, target)
            right = self.findNode(node.right, target)
            return left if left else right

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.populatePC(root)
        target = self.findNode(root, start)
        time = -1
        dq = deque()
        dq.append(target)
        visited = set()
        visited.add(target)
        while dq:
            n = len(dq)
            for _ in range(n):
                node = dq.popleft()
                if node.left and node.left not in visited:
                    visited.add(node.left)
                    dq.append(node.left)
                
                if node.right and node.right not in visited:
                    visited.add(node.right)
                    dq.append(node.right)
                
                parent = self.pc[node] if node in self.pc else None
                if parent and parent not in visited:
                    visited.add(parent)
                    dq.append(parent)
            time += 1
        return time