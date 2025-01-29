class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        if (startPos - endPos) % 2 != k % 2 or abs(startPos - endPos) > k:
            return 0
        diff = abs(startPos - endPos)
        n = k
        r = (k + diff) // 2
        if r < 0 or r > n:
            return 0

        res = 1
        mod = 10**9 + 7
        for i in range(r):
            res = (res * (n - i)) % mod
            res = (res * pow(i + 1, mod - 2, mod)) % mod
        return res