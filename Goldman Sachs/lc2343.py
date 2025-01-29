class Solution:
    def smallestTrimmedNumbers(self, nums: list[str], queries: list[list[int]]) -> list[int]:
        ans, trimmed = [], {}
        for k, trim in queries:
            trimmed.setdefault(trim, sorted([(num[-trim :], i) for i, num in enumerate(nums)]))
            ans.append(trimmed[trim][k - 1][1])
        return ans