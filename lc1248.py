from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count_odd = [0] * (n + 1)
        count_odd[0] = 1
        odd_count = 0
        nice_count = 0

        for num in nums:
            if num % 2 == 1:
                odd_count += 1
            if odd_count >= k:
                nice_count += count_odd[odd_count - k]
            count_odd[odd_count] += 1
        
        return nice_count