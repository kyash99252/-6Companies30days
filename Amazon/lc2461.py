from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        freq = defaultdict(int)
        not_unique = subarr_sum = 0
        max_sum = 0
        for i in range(k):
            freq[nums[i]] += 1
            subarr_sum += nums[i]
            if freq[nums[i]] == 2:
                not_unique += 1
        
        if not_unique == 0:
            max_sum = subarr_sum
        
        left, right = 0, k
        while right < len(nums):
            subarr_sum += (nums[right] - nums[left])

            freq[nums[left]] -= 1
            if freq[nums[left]] == 1:
                not_unique -= 1
            
            freq[nums[right]] += 1
            if freq[nums[right]] == 2:
                not_unique += 1
            else:
                if not_unique == 0:
                    max_sum = max(max_sum, subarr_sum)
            left += 1
            right += 1
        return max_sum