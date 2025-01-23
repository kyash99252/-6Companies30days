# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def dfs(self, root: TreeNode, distance: int, good_pairs: list[int]) -> list[int]:
        if root.left is None and root.right is None:
            return [1]
        else:
            left_leaves, right_leaves = [], []
            if root.left:
                left_leaves = self.dfs(root.left, distance, good_pairs)
            if root.right:
                right_leaves = self.dfs(root.right, distance, good_pairs)

            for i in left_leaves:
                for j in right_leaves:
                    if i + j <= distance:
                        good_pairs[0] += 1
                
            lst = [(i + 1) for i in left_leaves] + [(i + 1) for i in right_leaves]
            return lst

    def countPairs(self, root: TreeNode, distance: int) -> int:
        good_pairs = [0]
        self.dfs(root, distance, good_pairs)
        return good_pairs[0]
