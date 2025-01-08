class Solution:
    def __init__(self):
        from collections import defaultdict
        self.dp = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

    def solve(self, i: int, k: int, wasLastDown: int, jump: int) -> int:
        if i > k + 1:
            return 0
        if jump in self.dp[i][wasLastDown]:
            return self.dp[i][wasLastDown][jump]

        ans = (i == k)
        ans += self.solve(i + (1 << jump), k, 0, jump + 1)
        if i != 0 and not wasLastDown:
            ans += self.solve(i - 1, k, 1, jump)

        self.dp[i][wasLastDown][jump] = ans
        return ans

    def waysToReachStair(self, k: int) -> int:
        return self.solve(1, k, 0, 0)