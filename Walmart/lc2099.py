class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        temp = sorted(enumerate(nums), key=lambda x: -x[1])
        temp = temp[:k]
        temp.sort(key=lambda x: x[0])
        ans = []
        for i in range(k):
            ans.append(temp[i][1])
        return ans