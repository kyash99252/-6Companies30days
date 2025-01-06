from typing import List

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        inc_subarr = 0
        for right in range(n):
            for left in range(right + 1):
                last_elem = -1
                isIncremovable = True
                for i in range(n):
                    if left <= i <= right:
                        continue
                    if nums[i] <= last_elem:
                        isIncremovable = False
                        break
                    last_elem = nums[i]
                if isIncremovable:
                    inc_subarr += 1
        return inc_subarr