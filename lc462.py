from typing import List

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        median = nums[n // 2] if n % 2 else (nums[n // 2] + nums[n // 2 - 1]) // 2

        steps = 0
        for num in nums:
            steps += abs(num - median)
        return steps