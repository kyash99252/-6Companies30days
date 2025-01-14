class Solution:
    def __init__(self):
        self.wordSet = set()

    def topDown(self, s: str, dp: list[int], idx: int) -> bool:
        if idx == len(s):
            return True
        if dp[idx] != -1:
            return dp[idx]
        
        for end in range(idx + 1, len(s) + 1):
            if s[idx:end] in self.wordSet and self.topDown(s, dp, end):
                dp[idx] = True
                return True
        
        dp[idx] = False
        return False

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [-1] * len(s)
        self.wordSet = set(wordDict)
        return self.topDown(s, dp, 0)