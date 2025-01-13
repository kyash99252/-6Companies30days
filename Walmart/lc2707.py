class Solution:
    def topDown(self, s: str, wordSet: set, idx: int, dp: list[int]) -> int:
        if idx == len(s):
            return 0
        
        if dp[idx] != -1:
            return dp[idx]
        
        extra_chars = 1 + self.topDown(s, wordSet, idx + 1, dp)
        
        for j in range(idx + 1, len(s) + 1):
            if s[idx:j] in wordSet:
                extra_chars = min(extra_chars, self.topDown(s, wordSet, j, dp))
        
        dp[idx] = extra_chars
        return dp[idx]

    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        wordSet = set(dictionary)
        dp = [-1] * len(s)
        return self.topDown(s, wordSet, 0, dp)