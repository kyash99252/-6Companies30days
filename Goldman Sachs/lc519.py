import random

class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m * n
        self.flipped = {}

    def flip(self) -> list[int]:
        rand_index = random.randint(0, self.total - 1)
        self.total -= 1
        actual_index = self.flipped.get(rand_index, rand_index)
        self.flipped[rand_index] = self.flipped.get(self.total, self.total)
        return [actual_index // self.n, actual_index % self.n]

    def reset(self) -> None:
        self.total = self.m * self.n
        self.flipped.clear()


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()