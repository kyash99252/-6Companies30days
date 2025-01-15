class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(',')
        stack = []
        for node in preorder:
            stack.append(node)
            while len(stack) >= 3 and stack[-2:] == ['#', '#'] and stack[-3] != '#':
                stack = stack[:-3]
                stack.append('#')
        return stack == ['#']