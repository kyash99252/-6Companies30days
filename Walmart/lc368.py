class Solution:
    def topDown(self, nums: list[int], lastElem: int, idx: int) -> list[int]:
        if idx == len(nums):
            return []
        if (idx, lastElem) in dp:
            return dp[(idx, lastElem)]
        take = []
        if nums[idx] % lastElem == 0:
            take = [nums[idx]] + self.topDown(nums, nums[idx], idx + 1)
        not_take = self.topDown(nums, lastElem, idx + 1)
        dp[(idx, lastElem)] = take if len(take) > len(not_take) else not_take
        return dp[(idx, lastElem)]

    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        global dp
        dp = {}
        nums.sort()
        return self.topDown(nums, 1, 0)