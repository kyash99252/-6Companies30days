from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        else:
            res = ''
            dq = deque()
            dq.append(root)
            while dq:
                n = len(dq)
                for _ in range(n):
                    node = dq.popleft()
                    if node:
                        res += str(node.val) + ','
                        dq.append(node.left)
                        dq.append(node.right)
                    else:
                        res += '#,'
            return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None 
        values = data.split(',') 
        root = TreeNode(int(values[0]))
        queue = deque([root])
        i = 1
        while queue:
            node = queue.popleft()
            if i < len(values)  and values[i] != '#':
                node.left = TreeNode(int(values[i])) 
                queue.append(node.left)
            i += 1
            if i < len(values)  and values[i] != '#':
                node.right = TreeNode(int(values[i]))
                queue.append(node.right) 
            i += 1
        return root

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))