import random

class Solution:

    def __init__(self, rects: list[list[int]]):
        self.rects = rects
        self.areas = []
        total_area = 0
        for a, b, x, y in rects:
            area = (x - a + 1) * (y - b + 1)
            total_area += area
            self.areas.append(total_area)

    def pick(self) -> list[int]:
        rand_val = random.randint(1, self.areas[-1])
        left, right = 0, len(self.areas) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.areas[mid] < rand_val:
                left = mid + 1
            else:
                right = mid - 1
        a, b, x, y = self.rects[left]
        rand_x = random.randint(a, x)
        rand_y = random.randint(b, y)
        return [rand_x, rand_y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()