
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def linkdelete(self, head, n, m):
        # Code here
        if n == 0:
            return
        elif m == 0:
            head = None
        else:
            curr, prev = head, None
            M, N = m, n
            while curr:
                m, n = M, N
                while m and curr:
                    m -= 1
                    prev = curr
                    curr = curr.next
                while n and curr:
                    prev.next = curr.next
                    curr = curr.next
                    n -= 1
            return head