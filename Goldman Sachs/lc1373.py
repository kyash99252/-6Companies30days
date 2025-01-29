# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        max_sum = 0

        def traverse(node):
            nonlocal max_sum
            if not node:
                return float('inf'), float('-inf'), 0
            
            left_min, left_max, left_sum = traverse(node.left)
            right_min, right_max, right_sum = traverse(node.right)

            if left_max < node.val < right_min:
                current_sum = left_sum + right_sum + node.val
                max_sum = max(max_sum, current_sum)
                return min(left_min, node.val), max(right_max, node.val), current_sum
            else:
                return float('-inf'), float('inf'), 0

        traverse(root)
        return max_sum