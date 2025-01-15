class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        n, m = len(nums1), len(nums2)
        memo = [[0] * (m + 1) for _ in range(n + 1)]
        ans = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    memo[i][j] = memo[i - 1][j - 1] + 1
                    ans = max(ans, memo[i][j])
        
        return ans