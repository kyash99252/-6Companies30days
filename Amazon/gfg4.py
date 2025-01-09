class Solution:
    def matrixChainOrder(self, arr):
        # code here
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        brackets = [[None] * n for _ in range(n)]

        def constructOptimalOrder(i, j):
            if i == j:
                return chr(65 + i - 1)
            return f"({constructOptimalOrder(i, brackets[i][j])}{constructOptimalOrder(brackets[i][j] + 1, j)})"

        for length in range(2, n):
            for i in range(1, n - length + 1):
                j = i + length - 1
                dp[i][j] = float("inf")
                for k in range(i, j):
                    cost = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                    if cost < dp[i][j]:
                        dp[i][j] = cost
                        brackets[i][j] = k

        return constructOptimalOrder(1, n - 1)