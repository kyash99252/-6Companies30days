class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = [i for i in range(1, n + 1)]
        ptr = 0
        while len(circle) > 1:
            ptr = (ptr + k - 1) % len(circle)
            circle.pop(ptr)
        return circle[0]